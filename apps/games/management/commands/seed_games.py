"""بازی‌های سایت قدیم (مار، ۲۰۴۸، حدس کلمات) + امتیازهای ثبت‌شده‌ی قبلی.

    python manage.py seed_games
"""
import json
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.core.models import HomeSection, NavLink
from apps.games.models import Game, Score

SEED = Path(__file__).resolve().parents[2] / "seed"

GAMES = [
    {"slug": "snake", "engine": "snake", "title": "مار", "emoji": "🐍", "order": 1,
     "summary": "بازی کلاسیک مار؛ غذا بخور، بزرگ شو و به دیوار نخور.",
     "how_to": "با کلیدهای جهت‌نما یا کشیدن انگشت، مار را هدایت کنید. غذای قرمز را بخورید تا بزرگ‌تر شوید. به خودتان یا دیوار نخورید!"},
    {"slug": "2048", "engine": "2048", "title": "۲۰۴۸", "emoji": "🔢", "order": 2, "difficulty": "medium",
     "summary": "کاشی‌های هم‌عدد را با هم ترکیب کنید تا به ۲۰۴۸ برسید.",
     "how_to": "با کلیدهای جهت‌نما یا کشیدن انگشت، همه‌ی کاشی‌ها را جابه‌جا کنید. دو کاشی هم‌عدد که به هم برسند یکی می‌شوند."},
    {"slug": "words", "engine": "wordle-fa", "title": "حدس کلمات", "emoji": "🔤", "order": 3, "difficulty": "medium",
     "summary": "وردل فارسی: کلمه‌ی ۵ حرفی را در ۶ حدس پیدا کنید.",
     "how_to": "یک کلمه‌ی ۵ حرفی بنویسید و «تأیید» بزنید. سبز یعنی حرف درست در جای درست، زرد یعنی حرف در کلمه هست ولی جای دیگر، خاکستری یعنی این حرف در کلمه نیست."},
]
OLD_KEYS = {"snake": "snake", "2048": "2048", "words": "words"}


class Command(BaseCommand):
    help = "ساخت بازی‌ها و انتقال امتیازهای سایت قدیم"

    @transaction.atomic
    def handle(self, *args, **opts):
        scores = json.loads((SEED / "scores.json").read_text(encoding="utf-8")) if (SEED / "scores.json").exists() else {}
        for g in GAMES:
            game, created = Game.objects.get_or_create(slug=g["slug"], defaults={k: v for k, v in g.items() if k != "slug"})
            if created:
                n = 0
                for s in scores.get(OLD_KEYS[g["slug"]], []):
                    obj = Score.objects.create(game=game, player_name=s["player_name"][:40], score=int(s["score"]))
                    try:
                        dt = timezone.make_aware(datetime.fromisoformat(s["created_at"]))
                        Score.objects.filter(pk=obj.pk).update(created_at=dt)
                    except (ValueError, KeyError):
                        pass
                    n += 1
                Game.objects.filter(pk=game.pk).update(play_count=n)
                self.stdout.write(self.style.SUCCESS(f"✓ {game.title} ({n} امتیاز قدیمی)"))
        NavLink.objects.get_or_create(url="/games/", defaults={"title": "بازی", "order": 3})
        if not HomeSection.objects.filter(key="games").exists():
            last = HomeSection.objects.order_by("-order").first()
            HomeSection.objects.create(key="games", kicker="بازی کن", title="یک استراحت کوتاه",
                                       subtitle="بازی‌های ساده‌ی مرورگری با جدول امتیازات.", items_limit=3,
                                       is_active=False, order=(last.order + 5 if last else 100))
            self.stdout.write("✓ بخش «بازی‌ها» به صفحه‌ی اصلی اضافه شد (خاموش؛ از پنل روشن کنید)")
