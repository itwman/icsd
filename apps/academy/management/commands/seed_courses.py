"""
بارگذاری دوره‌های پیش‌فرض از apps/academy/seed/courses/*.py
اجرا:  python manage.py seed_courses
       python manage.py seed_courses --overwrite   (محتوای موجود را بازنویسی می‌کند)
"""
import importlib
import pkgutil

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from apps.academy import seed
from apps.academy.models import Category, Course, Lesson, Module
from apps.blog.models import Tag


class Command(BaseCommand):
    help = "بارگذاری دوره‌های آموزشی پیش‌فرض"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true", help="دوره‌های موجود را بازنویسی کن")

    def handle(self, *args, **opts):
        pkg = importlib.import_module("apps.academy.seed.courses")
        total_c = total_l = 0
        for info in pkgutil.iter_modules(pkg.__path__):
            mod = importlib.import_module(f"apps.academy.seed.courses.{info.name}")
            data = getattr(mod, "COURSE", None)
            if not data:
                continue
            exists = Course.objects.filter(slug=data["slug"]).exists()
            if exists and not opts["overwrite"]:
                self.stdout.write(f"· {data['title']} — قبلاً هست، رد شد")
                continue
            self._load(data, overwrite=exists)
            total_c += 1
            total_l += sum(len(m["lessons"]) for m in data["modules"])
            self.stdout.write(self.style.SUCCESS(f"✓ {data['title']}"))
        self.stdout.write(self.style.SUCCESS(f"\n{total_c} دوره و {total_l} درس بارگذاری شد."))

    def _load(self, d, overwrite=False):
        cat, _ = Category.objects.get_or_create(
            title=d["category"], defaults={"slug": slugify(d["category"], allow_unicode=True)})
        course, _ = Course.objects.update_or_create(slug=d["slug"], defaults={
            "title": d["title"], "category": cat, "level": d.get("level", "beginner"),
            "summary": d.get("summary", "")[:250], "description": d.get("description", ""),
            "price": 0, "duration_minutes": d.get("duration_minutes", 0),
            "is_published": True,
        })
        for t in d.get("tags", []):
            tag, _ = Tag.objects.get_or_create(name=t)
            course.tags.add(tag)
        if overwrite:
            course.modules.all().delete()
        for mi, m in enumerate(d["modules"]):
            module = Module.objects.create(course=course, title=m["title"], order=mi)
            for li, l in enumerate(m["lessons"]):
                Lesson.objects.create(
                    module=module, title=l["title"], order=li,
                    kind=l.get("kind", "text"), minutes=l.get("minutes", 10),
                    is_preview=bool(l.get("is_preview")), body=l.get("body", ""),
                    video_source="none",
                )
