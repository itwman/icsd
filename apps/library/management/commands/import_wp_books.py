"""انتقال کتاب‌های کتابخانه‌ی دیجیتال وردپرس (seed/books.json + seed/covers).

    python manage.py import_wp_books              # فقط کتاب‌های جدید
    python manage.py import_wp_books --overwrite  # به‌روزرسانی همه

آدرس‌های قدیمی /books/<نامک>/ با ریدایرکت ۳۰۱ به /library/<نامک>/ می‌روند.
"""
import json
from datetime import date
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from apps.core.models import HomeSection, NavLink
from apps.library.models import Book, BookCategory
from apps.seo.models import Redirect

SEED = Path(__file__).resolve().parents[2] / "seed"


class Command(BaseCommand):
    help = "انتقال کتاب‌های وردپرس به کتابخانه‌ی دیجیتال"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true")

    @transaction.atomic
    def handle(self, *args, **opts):
        data = json.loads((SEED / "books.json").read_text(encoding="utf-8"))
        made = upd = 0
        for d in data:
            cat = None
            if d.get("category"):
                c = d["category"]
                cat, _ = BookCategory.objects.get_or_create(slug=slugify(c["slug"], allow_unicode=True)[:100], defaults={"title": c["name"]})
            book = Book.objects.filter(slug=d["slug"]).first()
            if book and not opts["overwrite"]:
                self._redirect(d["old_path"], book)
                continue
            if book:
                upd += 1
            else:
                book = Book(slug=d["slug"])
                made += 1
            for f in ("title", "kind", "authors", "translator", "publisher", "year", "edition", "pages", "language",
                      "excerpt", "description", "download_url", "preview_url", "file_size", "cover_alt"):
                setattr(book, f, d.get(f) or ("" if f != "pages" else None))
            book.category = cat
            book.file_format = "pdf"
            book.published_at = date.fromisoformat(d["date"])
            book.is_published = True
            cover = SEED / "covers" / d["cover"] if d.get("cover") else None
            if cover and cover.is_file() and (opts["overwrite"] or not book.cover):
                with cover.open("rb") as fh:
                    book.cover.save(cover.name, File(fh), save=False)
            book.save()
            self._redirect(d["old_path"], book)
            self.stdout.write(self.style.SUCCESS(f"✓ {book.title}"))

        Redirect.objects.update_or_create(old_path="/books/", defaults={"new_path": "/library/", "status_code": 301, "is_active": True})
        NavLink.objects.get_or_create(url="/library/", defaults={"title": "کتابخانه", "order": 3})
        if not HomeSection.objects.filter(key="library").exists():
            blog = HomeSection.objects.filter(key="blog").first()
            HomeSection.objects.create(key="library", kicker="کتابخانه", title="کتاب‌های رایگان ICSD",
                                       subtitle="کتاب‌های الکترونیکی که نوشته‌ایم؛ دانلود رایگان PDF.", items_limit=4,
                                       order=(blog.order + 1 if blog else 90))
            self.stdout.write("✓ بخش «کتابخانه» به صفحه‌ی اصلی اضافه شد")
        self.stdout.write(self.style.SUCCESS(f"\n{made} کتاب ساخته و {upd} کتاب به‌روز شد."))

    @staticmethod
    def _redirect(old, book):
        Redirect.objects.update_or_create(old_path=old, defaults={"new_path": book.get_absolute_url(), "status_code": 301, "is_active": True})
