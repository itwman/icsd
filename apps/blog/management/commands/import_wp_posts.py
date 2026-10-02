"""انتقال مقاله‌های وردپرس icsd.ir (فایل seed/posts.json + تصاویر seed/images).

    python manage.py import_wp_posts              # فقط مقاله‌های جدید
    python manage.py import_wp_posts --overwrite  # به‌روزرسانی همه

- آدرس قدیمی هر مقاله (مثل /tarahi-site-farsh-kashan/) با ریدایرکت ۳۰۱ به /blog/<نامک>/ می‌رود.
- عنوان و توضیح متای Rank Math هم منتقل می‌شود؛ کلیدواژه‌ی کانونی از عنوان سئو حدس زده شده و قابل ویرایش است.
- تصاویر داخل متن به media/blog/import/ کپی و آدرس‌ها اصلاح می‌شوند.
"""
import json
import shutil
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.blog.models import BlogCategory, Post, Tag
from apps.seo.models import Redirect

SEED = Path(__file__).resolve().parents[2] / "seed"
CATS = {"carpet-industry": "صنعت فرش", "artificial-intelligence": "هوش مصنوعی", "office-automation": "اتوماسیون",
        "content-production": "تولید محتوا", "decoration": "دکوراسیون"}


def aware(s):
    dt = datetime.fromisoformat(s)
    return timezone.make_aware(dt) if timezone.is_naive(dt) else dt


class Command(BaseCommand):
    help = "انتقال مقاله‌های وردپرس با تصاویر، سئو و ریدایرکت"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true")

    @transaction.atomic
    def handle(self, *args, **opts):
        data = json.loads((SEED / "posts.json").read_text(encoding="utf-8"))
        media_dir = Path(settings.MEDIA_ROOT) / "blog" / "import"
        media_dir.mkdir(parents=True, exist_ok=True)
        media_url = settings.MEDIA_URL.rstrip("/") + "/blog/import/"
        made = upd = red = 0
        for d in data:
            cat, _ = BlogCategory.objects.get_or_create(slug=d["category"], defaults={"title": CATS.get(d["category"], d["category"])})
            post = Post.objects.filter(slug=d["slug"]).first()
            if post and not opts["overwrite"]:
                Redirect.objects.update_or_create(old_path=d["old_path"], defaults={"new_path": post.get_absolute_url(), "status_code": 301, "is_active": True})
                continue
            body = d["body"]
            for img in (SEED / "images").iterdir() if (SEED / "images").exists() else []:
                if f"@@MEDIA@@{img.name}" in body:
                    target = media_dir / img.name
                    if not target.exists():
                        shutil.copyfile(img, target)
                    body = body.replace(f"@@MEDIA@@{img.name}", media_url + img.name)
            if post:
                upd += 1
            else:
                post = Post(slug=d["slug"])
                made += 1
            post.title, post.category, post.body = d["title"], cat, body
            post.excerpt = d["excerpt"][:300]
            post.published_at = aware(d["date"])
            post.read_minutes = d["read_minutes"]
            post.is_published = True
            post.seo_title, post.meta_description, post.focus_keyword = d["seo_title"], d["meta_description"], d["focus_keyword"]
            post.noindex = d["noindex"]
            post.cover_alt = d.get("cover_alt", "")[:200]
            cover = SEED / "images" / d["cover"] if d.get("cover") else None
            if cover and cover.is_file() and (opts["overwrite"] or not post.cover):
                with cover.open("rb") as fh:
                    post.cover.save(cover.name, File(fh), save=False)
            post.save()
            post.tags.set([Tag.objects.get_or_create(name=t)[0] for t in d["tags"]])
            _, c = Redirect.objects.update_or_create(old_path=d["old_path"], defaults={"new_path": post.get_absolute_url(), "status_code": 301, "is_active": True})
            red += c
            self.stdout.write(self.style.SUCCESS(f"✓ {post.title[:70]}"))
        # فید وردپرس
        Redirect.objects.update_or_create(old_path="/feed/", defaults={"new_path": "/blog/feed/", "status_code": 301, "is_active": True})
        self.stdout.write(self.style.SUCCESS(f"\n{made} مقاله ساخته، {upd} به‌روز و {red} ریدایرکت جدید ثبت شد."))
