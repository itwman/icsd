# داده: روی سایتی که از قبل بخش‌های صفحه‌ی اصلی را دارد، بخش‌های «سیلک»، «نوار سفال» و «مشتریان» را اضافه می‌کند.
# روی دیتابیس تازه کاری نمی‌کند؛ آن‌جا seed_site همه‌ی بخش‌ها را می‌سازد.

from django.db import migrations

NEW = {
    "sialk": ("TAPPEH SIALK · KASHAN · 33.97°N 51.40°E", "تپه‌های شمالی و جنوبی سیلک — هفت هزار سال لایه، و شبکه‌ای که آن‌ها را می‌خواند", ""),
    "band": ("", "نوار نقش سفال سیلک", ""),
    "customers": ("مشتریان", "کسانی که با ما کار می‌کنند", "کارخانه‌ها، بازرگانان و سازمان‌هایی که نرم‌افزارهای ما هر روز در کارشان است."),
}
LIMITS = {"products": 8, "customers": 0, "academy": 6, "blog": 3}


def forwards(apps, schema_editor):
    HomeSection = apps.get_model("core", "HomeSection")
    existing = list(HomeSection.objects.order_by("order", "id"))
    if not existing:
        return
    keys = {s.key for s in existing}
    seq = []
    for k in ("sialk", "band"):
        if k not in keys:
            kick, title, sub = NEW[k]
            seq.append(HomeSection(key=k, kicker=kick, title=title, subtitle=sub))
    for s in existing:
        seq.append(s)
        if s.key == "products" and "customers" not in keys:
            kick, title, sub = NEW["customers"]
            seq.append(HomeSection(key="customers", kicker=kick, title=title, subtitle=sub))
    for i, s in enumerate(seq):
        s.order = i * 10
        if s.key in LIMITS:
            s.items_limit = LIMITS[s.key]
        s.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_homesection_items_customer"),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
