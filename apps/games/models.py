from django.conf import settings
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.seo.models import SEOFields

DEFAULT_WORDS = """ایران
ستاره
فرهنگ
سلامت
تاریخ
ریاضی
سفارش
محصول
گزارش
تحلیل
سیستم
تجربه
ترجمه
نوشته
پرنده
حیوان
مدارس
جلسات
مهاجر
ماشین
کاشان
بادام
باغچه
پنجره
دریچه
مسافر
استاد
مدرسه
پارچه
نساجی
کارگر
تولید
بازار
تجارت
مشتری
دیوار
پاییز
شکوفه
گلدان
شیرین
لبخند
دوستی
پرواز
کبوتر
شاهین
دلفین
خرگوش
روباه
زرافه
جزیره
انگور
نارنج
کلوچه
منطقی
ماژول
متغیر
امنیت
پروژه
طراحی
توسعه
کیفیت
بودجه
سیاره
باران
طوفان
رنگین
نقاشی
شاعری
دیوان
قصیده
کتیبه
سفالی
میراث
فرشته
بافتن
گلابی
مناره"""


class Game(SEOFields, models.Model):
    ENGINES = [("snake", "مار"), ("2048", "۲۰۴۸"), ("wordle-fa", "حدس کلمات (وردل فارسی)")]
    LEVELS = [("easy", "آسان"), ("medium", "متوسط"), ("hard", "سخت")]
    MAX_SCORE = {"snake": 20000, "2048": 2000000, "wordle-fa": 1000}

    title = models.CharField("نام بازی", max_length=80)
    slug = models.SlugField("نامک (در آدرس)", max_length=80, unique=True, allow_unicode=True)
    engine = models.CharField("موتور بازی", max_length=12, choices=ENGINES)
    summary = models.CharField("معرفی یک‌خطی", max_length=200, blank=True)
    how_to = models.TextField("راهنمای بازی", blank=True)
    description = CKEditor5Field("توضیح کامل (زیر بازی)", config_name="default", blank=True)
    difficulty = models.CharField("سختی", max_length=8, choices=LEVELS, default="easy")
    color = models.CharField("رنگ", max_length=7, default="#1E9E7B")
    emoji = models.CharField("نماد", max_length=8, default="🎮")
    cover = models.ImageField("تصویر", upload_to="games/", blank=True)
    words = models.TextField("فهرست کلمات (فقط حدس کلمات)", blank=True, default=DEFAULT_WORDS,
                             help_text="هر خط یک کلمه‌ی ۵ حرفی فارسی، بدون نیم‌فاصله و «آ». کلمه‌های غیر ۵ حرفی نادیده گرفته می‌شوند.")
    leaderboard_size = models.PositiveSmallIntegerField("تعداد نفرات جدول امتیازات", default=10)
    play_count = models.PositiveIntegerField("تعداد بازی", default=0)
    is_active = models.BooleanField("فعال", default=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "بازی"
        verbose_name_plural = "بازی‌ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("games:detail", args=[self.slug])

    @property
    def body(self):
        return self.description or self.how_to

    @property
    def word_list(self):
        return [w.strip() for w in (self.words or "").splitlines() if len(w.strip()) == 5 and "‌" not in w]

    def top_scores(self, limit=None):
        return self.scores.filter(is_hidden=False).order_by("-score", "created_at")[: limit or self.leaderboard_size]


class Score(models.Model):
    game = models.ForeignKey(Game, verbose_name="بازی", on_delete=models.CASCADE, related_name="scores")
    player_name = models.CharField("نام بازیکن", max_length=40)
    score = models.PositiveIntegerField("امتیاز")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", null=True, blank=True, on_delete=models.SET_NULL)
    ip_hash = models.CharField("هش IP", max_length=64, blank=True)
    is_hidden = models.BooleanField("پنهان (تقلب/نام نامناسب)", default=False)
    created_at = models.DateTimeField("زمان", auto_now_add=True)

    class Meta:
        ordering = ["-score"]
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازها"

    def __str__(self):
        return f"{self.player_name} — {self.score}"
