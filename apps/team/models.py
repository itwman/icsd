from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.seo.models import SEOFields


class TeamMember(SEOFields, models.Model):
    """عضو تیم + رزومه‌ی کامل (تحصیلات، سوابق، مقالات، مهارت‌ها، شبکه‌ها)."""
    name = models.CharField("نام و نام خانوادگی", max_length=120)
    slug = models.SlugField("نامک (در آدرس)", unique=True, allow_unicode=True, help_text="مثل itwman → /team/itwman/")
    name_en = models.CharField("نام لاتین", max_length=120, blank=True)
    role = models.CharField("سمت", max_length=120)
    role_en = models.CharField("سمت (لاتین)", max_length=120, blank=True)
    degree = models.CharField("آخرین مدرک", max_length=60, blank=True, help_text="مثل کارشناسی ارشد")
    photo = models.ImageField("تصویر", upload_to="team/", blank=True, help_text="مربع، دست‌کم ۴۰۰×۴۰۰ پیکسل.")
    about = CKEditor5Field("درباره", blank=True, config_name="default")
    birth_year = models.CharField("سال تولد", max_length=4, blank=True)
    city = models.CharField("محل سکونت", max_length=80, blank=True)
    email = models.EmailField("ایمیل", blank=True)
    phone = models.CharField("تلفن", max_length=20, blank=True)
    website = models.URLField("وب‌سایت", blank=True)
    show_contact = models.BooleanField("نمایش اطلاعات تماس", default=True, help_text="ایمیل و تلفن در صفحه‌ی رزومه نمایش داده شود.")
    show_birth_year = models.BooleanField("نمایش سال تولد", default=True)
    is_active = models.BooleanField("فعال", default=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "عضو تیم"
        verbose_name_plural = "اعضای تیم"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("team:detail", args=[self.slug])

    @property
    def skill_groups(self):
        groups = {}
        for s in self.skills.all():
            groups.setdefault(s.group or "سایر", []).append(s)
        return groups.items()


class _Item(models.Model):
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class Education(_Item):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="education")
    title = models.CharField("مقطع و رشته", max_length=200, help_text="مثل کارشناسی ارشد - مهندسی کامپیوتر - نرم‌افزار")
    org = models.CharField("دانشگاه / مؤسسه", max_length=200, blank=True)
    start = models.CharField("از سال", max_length=10, blank=True)
    end = models.CharField("تا سال", max_length=10, blank=True)
    desc = models.CharField("پایان‌نامه / توضیح", max_length=300, blank=True)

    class Meta(_Item.Meta):
        verbose_name = "تحصیلات"
        verbose_name_plural = "تحصیلات"


class Experience(_Item):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="experience")
    title = models.CharField("سمت", max_length=200)
    org = models.CharField("سازمان • شهر", max_length=200, blank=True)
    start = models.CharField("از سال", max_length=10, blank=True)
    end = models.CharField("تا سال", max_length=10, blank=True, help_text="خالی یا «تاکنون»")
    desc = models.CharField("توضیح", max_length=300, blank=True)

    class Meta(_Item.Meta):
        verbose_name = "سابقه‌ی کاری"
        verbose_name_plural = "سوابق کاری"


class Publication(_Item):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="publications")
    title = models.CharField("عنوان", max_length=300)
    url = models.URLField("پیوند", blank=True)
    authors = models.CharField("همکاران", max_length=300, blank=True)
    venue = models.CharField("کنفرانس / نشریه", max_length=300, blank=True)
    year = models.CharField("سال", max_length=10, blank=True)

    class Meta(_Item.Meta):
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


class Skill(_Item):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="skills")
    group = models.CharField("گروه", max_length=60, blank=True, help_text="مثل Programming، CMS، Graphic")
    name = models.CharField("مهارت", max_length=80)
    level = models.PositiveSmallIntegerField("سطح (٪)", default=70)

    class Meta(_Item.Meta):
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت‌ها"


class SocialLink(_Item):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name="socials")
    label = models.CharField("نام شبکه", max_length=40, help_text="LinkedIn، GitHub، Telegram، ...")
    url = models.URLField("آدرس")

    class Meta(_Item.Meta):
        verbose_name = "شبکه‌ی اجتماعی"
        verbose_name_plural = "شبکه‌های اجتماعی"
