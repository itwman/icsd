"""اعضای تیم و رزومه‌ها از icsd.ir/team (فایل seed/team.json + تصاویر seed/photos).

    python manage.py seed_team              # فقط اعضای جدید
    python manage.py seed_team --overwrite  # به‌روزرسانی همه از فایل seed
"""
import json
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.core.models import HomeSection, NavLink
from apps.team.models import TeamMember

SEED = Path(__file__).resolve().parents[2] / "seed"


class Command(BaseCommand):
    help = "ساخت اعضای تیم با رزومه"

    def add_arguments(self, parser):
        parser.add_argument("--overwrite", action="store_true")

    @transaction.atomic
    def handle(self, *args, **opts):
        data = json.loads((SEED / "team.json").read_text(encoding="utf-8"))
        for i, d in enumerate(data):
            m = TeamMember.objects.filter(slug=d["slug"]).first()
            if m and not opts["overwrite"]:
                continue
            m = m or TeamMember(slug=d["slug"])
            m.name, m.name_en, m.role, m.role_en, m.degree = d["name"], d["name_en"], d["role"], d["role_en"], d["degree"]
            m.about = d["about"] if d["about"].startswith("<") else f"<p>{d['about']}</p>"
            m.birth_year, m.city, m.email, m.phone, m.website = d["birth_year"], d["city"], d["email"], d["phone"], d["website"]
            m.order, m.is_active = i, True
            m.seo_title = f"{d['name']} | {d['role']}"[:70]
            photo = SEED / "photos" / d.get("photo_file", "")
            if photo.is_file() and (opts["overwrite"] or not m.photo):
                with photo.open("rb") as fh:
                    m.photo.save(photo.name, File(fh), save=False)
            m.save()
            for rel in ("education", "experience", "publications", "skills", "socials"):
                getattr(m, rel).all().delete()
            for j, e in enumerate(d["education"]):
                m.education.create(title=e["title"], org=e["org"], start=e["start"], end=e["end"], desc=e["desc"], order=j)
            for j, e in enumerate(d["experience"]):
                m.experience.create(title=e["title"], org=e["org"], start=e["start"], end=e["end"], desc=e["desc"], order=j)
            for j, p in enumerate(d["publications"]):
                m.publications.create(title=p["title"], url=p["url"], authors=p["authors"], venue=p["venue"], year=p["year"], order=j)
            for j, s in enumerate(d["skills"]):
                m.skills.create(group=s["group"], name=s["name"], level=s["level"], order=j)
            for j, (label, url) in enumerate(d["socials"]):
                m.socials.create(label=label, url=url, order=j)
            self.stdout.write(self.style.SUCCESS(f"✓ {m.name}"))
        if HomeSection.objects.exists() and not HomeSection.objects.filter(key="team").exists():
            after = HomeSection.objects.filter(key="customers").first() or HomeSection.objects.filter(key="products").first()
            HomeSection.objects.create(key="team", kicker="تیم", title="کسانی که ICSD را می‌سازند",
                                       subtitle="مهندسان و متخصصانی که از کاشان برای صنعت فرش و نساجی نرم‌افزار می‌نویسند.",
                                       order=(after.order + 5) if after else 100, items_limit=0)
            self.stdout.write("✓ بخش «تیم» به صفحه‌ی اصلی اضافه شد")
        if not NavLink.objects.filter(url="/team/").exists():
            NavLink.objects.create(title="تیم ما", url="/team/", order=NavLink.objects.count() * 10)
            self.stdout.write("✓ «تیم ما» به منو اضافه شد")
