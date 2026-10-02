from django.core.cache import cache
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.validators import CUSTOMER_LOGO_HELP, validate_customer_logo


class SingletonModel(models.Model):
    """فقط یک رکورد — برای تنظیمات سایت."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        cache.delete(self.cache_key())

    @classmethod
    def cache_key(cls):
        return f"singleton:{cls.__name__}"

    @classmethod
    def load(cls):
        obj = cache.get(cls.cache_key())
        if obj is None:
            obj, _ = cls.objects.get_or_create(pk=1)
            cache.set(cls.cache_key(), obj, 300)
        return obj


class SiteSettings(SingletonModel):
    """
    همه‌ی چیزهایی که ممکن است در آینده عوض شود: نام برند، لوگو، دامنه، رنگ، تماس، درگاه، پیامک.
    """
    # هویت
    site_name = models.CharField("نام سایت / برند", max_length=120, default="توسعه هوشمند فرش ایرانیان")
    short_name = models.CharField("نام کوتاه", max_length=40, default="ICSD")
    tagline = models.CharField("شعار", max_length=200, blank=True, default="کاشان هفت هزار سال است چیزی می‌سازد.")
    site_url = models.URLField("آدرس سایت", default="https://icsd.ir", help_text="بدون / انتها. در sitemap و لینک‌های مطلق استفاده می‌شود.")
    logo = models.ImageField("لوگو", upload_to="brand/", blank=True)
    logo_dark = models.ImageField("لوگو برای حالت شب", upload_to="brand/", blank=True)
    favicon = models.ImageField("فاوآیکن", upload_to="brand/", blank=True)
    founded_year = models.PositiveIntegerField("سال تأسیس (شمسی)", default=1396)

    # رنگ‌ها
    color_primary = models.CharField("رنگ اصلی", max_length=7, default="#1E9E7B")
    color_accent = models.CharField("رنگ تأکید", max_length=7, default="#16A9C7")

    # تماس
    phone = models.CharField("تلفن", max_length=40, blank=True)
    mobile = models.CharField("موبایل", max_length=20, blank=True)
    email = models.EmailField("ایمیل", blank=True)
    address = models.TextField("آدرس", blank=True, default="کاشان، ایران")
    map_embed = models.TextField("کد نقشه (iframe)", blank=True)
    instagram = models.URLField("اینستاگرام", blank=True)
    telegram = models.URLField("تلگرام", blank=True)
    linkedin = models.URLField("لینکدین", blank=True)
    aparat = models.URLField("آپارات", blank=True)

    # هیرو
    hero_title = models.CharField("تیتر هیرو", max_length=200, default="هفت هزار سال است این شهر چیزی می‌سازد.")
    hero_highlight = models.CharField("بخش رنگی تیتر", max_length=80, default="چیزی می‌سازد", help_text="این عبارت داخل تیتر با گرادیان رنگی نمایش داده می‌شود.")
    hero_subtitle = models.TextField("زیرتیتر هیرو", default="زیگورات سیلک، قنات، باغ فین، بادگیر — کاشان همیشه مهندسی کرده است. ما ادامه‌ی همان کاریم: نرم‌افزار اختصاصی برای کارخانه‌ها و بازرگانان صنعت فرش و نساجی.")
    hero_show_clock = models.BooleanField("نمایش ساعت و نمایشگر", default=True)
    hero_particles = models.BooleanField("کلمات ذره‌ای متحرک", default=True,
        help_text="کلمه‌ها از ذره ساخته می‌شوند، یکی‌یکی به هم تبدیل می‌شوند و با ماوس/لمس پراکنده می‌شوند.")
    hero_words = models.CharField("کلمات ذره‌ای", max_length=200, default="ایده|داده|هوش مصنوعی|نرم‌افزار",
        help_text="با | جدا کنید. بهتر است کوتاه باشند (۱ یا ۲ کلمه).")
    hero_words_logo = models.BooleanField("پایان با لوگو", default=True, help_text="بعد از آخرین کلمه، لوگوی شرکت از ذره‌ها ساخته شود.")
    hero_words_interval = models.PositiveSmallIntegerField("مکث هر کلمه (میلی‌ثانیه)", default=3200)
    stat_1_value = models.CharField("آمار ۱ — مقدار", max_length=20, default="۱۳۹۶")
    stat_1_label = models.CharField("آمار ۱ — برچسب", max_length=60, default="سال شروع، در کاشان")
    stat_2_value = models.CharField("آمار ۲ — مقدار", max_length=20, default="۸")
    stat_2_label = models.CharField("آمار ۲ — برچسب", max_length=60, default="محصول عملیاتی")
    stat_3_value = models.CharField("آمار ۳ — مقدار", max_length=20, default="۵۰+")
    stat_3_label = models.CharField("آمار ۳ — برچسب", max_length=60, default="کارخانه و بازرگانی")

    # فوتر و سئو
    footer_text = models.TextField("متن فوتر", blank=True, default="ارائه‌ی خدمات جامع فناوری اطلاعات برای صنعت فرش، نساجی و بازرگانی — کاشان، ایران.")
    default_meta_description = models.CharField("توضیح متای پیش‌فرض", max_length=300, blank=True)
    default_og_image = models.ImageField("تصویر پیش‌فرض اشتراک‌گذاری", upload_to="brand/", blank=True)
    head_extra_html = models.TextField("کد اضافی در head", blank=True, help_text="مثلاً کد تأیید سرچ کنسول. فقط مدیر ارشد.")
    enamad_html = models.TextField("کد اینماد", blank=True)

    # درگاه و پیامک (اگر خالی باشد از .env خوانده می‌شود)
    zarinpal_merchant_id = models.CharField("مرچنت زرین‌پال", max_length=64, blank=True)
    zarinpal_sandbox = models.BooleanField("حالت آزمایشی زرین‌پال", default=True)
    kavenegar_api_key = models.CharField("کلید API کاوه‌نگار", max_length=200, blank=True)
    kavenegar_sender = models.CharField("شماره فرستنده", max_length=20, blank=True)

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"

    @property
    def hero_words_list(self):
        return [w.strip() for w in (self.hero_words or "").split("|") if w.strip()]

    def __str__(self):
        return self.site_name


class HomeSection(models.Model):
    """بخش‌های صفحه اصلی — قابل چینش، روشن/خاموش، و با متن قابل ویرایش."""
    KEYS = [
        ("sialk", "منظره‌ی تپه سیلک (نوار تمام‌عرض)"),
        ("band", "نوار نقش سفال"),
        ("products", "محصولات"),
        ("customers", "مشتریان"),
        ("timeline", "خط زمان کاشان"),
        ("academy", "آکادمی"),
        ("blog", "مقالات"),
        ("cta", "فراخوان"),
        ("custom", "بخش سفارشی (متن آزاد)"),
    ]
    key = models.CharField("نوع بخش", max_length=20, choices=KEYS)
    kicker = models.CharField("برچسب کوچک بالای تیتر", max_length=60, blank=True)
    title = models.CharField("تیتر", max_length=150)
    subtitle = models.TextField("زیرتیتر", blank=True)
    body = CKEditor5Field("متن (برای بخش سفارشی)", blank=True, config_name="default")
    items_limit = models.PositiveSmallIntegerField("حداکثر تعداد آیتم", default=8,
        help_text="برای محصولات، مشتریان، دوره‌ها و مقالات. ۰ یعنی همه.")
    button_text = models.CharField("متن دکمه", max_length=40, blank=True, help_text="خالی = دکمه‌ی پیش‌فرض بخش")
    button_url = models.CharField("آدرس دکمه", max_length=200, blank=True)
    is_active = models.BooleanField("فعال", default=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "بخش صفحه اصلی"
        verbose_name_plural = "بخش‌های صفحه اصلی"

    def __str__(self):
        return f"{self.get_key_display()} — {self.title}"

    def limit(self, qs):
        return qs[: self.items_limit] if self.items_limit else qs


class TimelineEvent(models.Model):
    """خط زمان فنی کاشان: از سیلک تا سرور."""
    era = models.CharField("دوره / سال", max_length=60)
    title = models.CharField("عنوان", max_length=120)
    text = models.TextField("توضیح")
    color = models.CharField("رنگ نقطه", max_length=7, default="#1E9E7B")
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "رویداد خط زمان"
        verbose_name_plural = "خط زمان کاشان"

    def __str__(self):
        return f"{self.era} — {self.title}"


class Page(models.Model):
    """صفحات ایستا: درباره ما، قوانین، حریم خصوصی و ..."""
    title = models.CharField("عنوان", max_length=150)
    slug = models.SlugField("نامک (در آدرس)", unique=True, allow_unicode=True)
    body = CKEditor5Field("متن", config_name="default")
    show_in_footer = models.BooleanField("نمایش در فوتر", default=True)
    is_published = models.BooleanField("منتشر شده", default=True)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "صفحه"
        verbose_name_plural = "صفحات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:page", args=[self.slug])


class NavLink(models.Model):
    """منوی اصلی سایت."""
    title = models.CharField("عنوان", max_length=60)
    url = models.CharField("آدرس", max_length=200, help_text="مثلاً /courses/ یا https://...")
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    is_active = models.BooleanField("فعال", default=True)
    new_tab = models.BooleanField("در تب جدید", default=False)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "آیتم منو"
        verbose_name_plural = "منو"

    def __str__(self):
        return self.title


class Customer(models.Model):
    """مشتریان شرکت — لوگو در صفحه‌ی اصلی (نوار متحرک) و صفحه‌ی «مشتریان»."""
    name = models.CharField("نام مشتری", max_length=120)
    logo = models.FileField("لوگو", upload_to="customers/", blank=True,
                            validators=[validate_customer_logo], help_text=CUSTOMER_LOGO_HELP)
    website = models.URLField("وب‌سایت", blank=True)
    city = models.CharField("شهر", max_length=60, blank=True)
    industry = models.CharField("حوزه‌ی فعالیت", max_length=80, blank=True, help_text="مثل: ریسندگی، فرش ماشینی، بازرگانی")
    description = models.TextField("توضیح کوتاه همکاری", blank=True, help_text="یک یا دو جمله؛ در صفحه‌ی مشتریان نمایش داده می‌شود.")
    products = models.ManyToManyField("products.Product", verbose_name="محصولات استفاده‌شده", blank=True, related_name="customers")
    since = models.CharField("شروع همکاری", max_length=20, blank=True, help_text="مثل ۱۴۰۲")
    show_on_home = models.BooleanField("نمایش در صفحه اصلی", default=True)
    is_active = models.BooleanField("فعال", default=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

    def __str__(self):
        return self.name
