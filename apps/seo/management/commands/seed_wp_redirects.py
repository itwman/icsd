"""ریدایرکت بخش‌های دیگر سایت وردپرسی قدیم: آموزش‌ها (/tutorials/) و درس‌هایشان → دوره‌های آکادمی.

    python manage.py seed_wp_redirects
"""
from django.core.management.base import BaseCommand

from apps.seo.models import Redirect

TUTORIALS = {
    "python-basics-tutorial": "/courses/python-basics/",
    "python-advanced-tutorial": "/courses/python-advanced/",
    "django-tutorial": "/courses/django/",
    "mysql-tutorial": "/courses/mysql/",
    "postgresql-tutorial": "/courses/postgresql/",
    "github-tutorial": "/courses/git-github/",
    "microservices-tutorial": "/courses/microservices/",
    "flutter-tutorial": "/courses/",
    "wordpress-tutorial": "/courses/",
    "woocommerce-tutorial": "/courses/",
}


class Command(BaseCommand):
    help = "ریدایرکت آموزش‌ها و درس‌های سایت قدیم به آکادمی"

    def handle(self, *args, **opts):
        n = 0
        rules = {"/tutorials/": "/courses/", "/tutorials/*": "/courses/", "/book_category/*": "/library/", "/games/words-fa/": "/games/words/"}
        for slug, target in TUTORIALS.items():
            rules[f"/tutorials/{slug}/"] = target
            rules[f"/tutorials/{slug}/*"] = target
        for old, new in rules.items():
            _, c = Redirect.objects.update_or_create(old_path=old, defaults={"new_path": new, "status_code": 301, "is_active": True})
            n += c
        self.stdout.write(self.style.SUCCESS(f"✓ {n} ریدایرکت جدید برای آموزش‌های قدیمی"))
