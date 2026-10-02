"""محصولات واقعی شرکت (از icsd.ir) با لوگوی استاندارد ۵۱۲×۵۱۲.

    python manage.py seed_products              # فقط محصولاتی که نیستند ساخته می‌شوند
    python manage.py seed_products --overwrite  # متن، وضعیت و لوگوی همه از فایل seed به‌روز می‌شود
                                                # و محصولات نمونه‌ی قدیمی (دوک، زال، ...) حذف می‌شوند

داده‌ها: apps/products/seed/products.json — لوگوها: apps/products/seed/logos/
"""
import json
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.products.models import Product

SEED = Path(__file__).resolve().parents[2] / "seed"
# محصولات نمونه‌ی نسخه‌ی اول که واقعی نبودند (یا نامک‌شان عوض شد)
OLD_SAMPLE_SLUGS = ["doox", "radman", "cheleh", "farshplus", "zaal"]
FIELDS = ["name", "latin_name", "tagline", "category_label", "color", "order", "is_featured", "summary",
          "description", "status", "version", "price_note", "demo_url", "tech_stack"]


class Command(BaseCommand):
    help = "ساخت/به‌روزرسانی محصولات واقعی شرکت با لوگو"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true", help="به‌روزرسانی محصولات موجود از فایل seed")

    @transaction.atomic
    def handle(self, *args, **opts):
        data = json.loads((SEED / "products.json").read_text(encoding="utf-8"))
        if opts["overwrite"]:
            n, _ = Product.objects.filter(slug__in=OLD_SAMPLE_SLUGS).delete()
            if n:
                self.stdout.write(f"· {n} رکورد از محصولات نمونه‌ی قدیمی حذف شد")
        made = updated = 0
        for d in data:
            p = Product.objects.filter(slug=d["slug"]).first()
            if p and not opts["overwrite"]:
                continue
            if not p:
                p = Product(slug=d["slug"])
                made += 1
            else:
                updated += 1
            for f in FIELDS:
                setattr(p, f, d.get(f, getattr(p, f)))
            p.license_label = d.get("license", "")
            p.is_active = True
            logo = SEED / "logos" / d["logo"]
            if logo.exists() and (opts["overwrite"] or not p.logo):
                with logo.open("rb") as fh:
                    p.logo.save(logo.name, File(fh), save=False)
            p.save()
            self.stdout.write(self.style.SUCCESS(f"✓ {p.name}"))
        self.stdout.write(self.style.SUCCESS(f"\n{made} محصول ساخته و {updated} محصول به‌روز شد."))
