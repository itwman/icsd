"""
نقش‌های پیش‌فرض:
  مدیر محتوا  → همه‌ی محتوا (دوره، محصول، وبلاگ، صفحات، بخش‌ها) بدون کاربران و تنظیمات حساس
  مدرس        → دوره/فصل/درس خودش + دیدن ثبت‌نام‌ها
  پشتیبانی    → درخواست‌های پروژه، سفارش‌ها، کاربران (فقط مشاهده/ویرایش)
اجرا: python manage.py setup_roles
"""
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

ROLES = {
    "مدیر محتوا": {
        "academy": ["category", "course", "module", "lesson", "enrollment", "quiz", "question", "choice", "attempt", "certificate"],
        "products": ["product", "productimage", "productfeature", "producttutorial"],
        "blog": ["post", "tag", "blogcategory"],
        "core": ["homesection", "timelineevent", "page", "navlink"],
        "seo": ["seometa", "redirect"],
    },
    "مدرس": {
        "academy": ["course", "module", "lesson", "quiz", "question", "choice"],
    },
    "پشتیبانی": {
        "leads": ["projectrequest", "province", "city"],
        "payments": ["order"],
        "accounts": ["user"],
    },
}
VIEW_ONLY = {"مدرس": {"academy": ["enrollment"]}, "پشتیبانی": {"analytics": ["pageview"]}}


class Command(BaseCommand):
    help = "ساخت گروه‌ها و مجوزهای پیش‌فرض"

    def handle(self, *args, **opts):
        for role, apps in ROLES.items():
            group, _ = Group.objects.get_or_create(name=role)
            perms = []
            for app, models in apps.items():
                for m in models:
                    perms += list(Permission.objects.filter(content_type__app_label=app, content_type__model=m))
            for app, models in VIEW_ONLY.get(role, {}).items():
                for m in models:
                    perms += list(Permission.objects.filter(content_type__app_label=app, content_type__model=m,
                                                            codename__startswith="view_"))
            group.permissions.set(perms)
            self.stdout.write(self.style.SUCCESS(f"✓ {role}: {len(perms)} مجوز"))
        self.stdout.write("برای اینکه کاربر به پنل وارد شود، is_staff را هم روشن کنید.")
