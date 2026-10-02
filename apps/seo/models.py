from django.db import models


class SEOMeta(models.Model):
    """
    متادیتا برای هر مسیر. اگر برای یک صفحه رکورد نباشد، از عنوان/خلاصه‌ی خود آبجکت استفاده می‌شود.
    مسیر مثل: /courses/django/  یا  /  یا  /blog/
    """
    path = models.CharField("مسیر", max_length=300, unique=True, help_text="با / شروع و تمام شود. مثل /courses/django/")
    title = models.CharField("عنوان (title)", max_length=120, blank=True)
    description = models.CharField("توضیح (meta description)", max_length=320, blank=True)
    keywords = models.CharField("کلیدواژه‌ها", max_length=300, blank=True)
    og_image = models.ImageField("تصویر اشتراک‌گذاری", upload_to="seo/", blank=True)
    canonical = models.URLField("آدرس کانونیکال", blank=True)
    noindex = models.BooleanField("noindex (از ایندکس خارج شود)", default=False)
    schema_json = models.TextField("JSON-LD اضافی", blank=True, help_text="اختیاری؛ یک آبجکت JSON معتبر.")

    class Meta:
        ordering = ["path"]
        verbose_name = "متادیتای صفحه"
        verbose_name_plural = "متادیتای صفحات"

    def __str__(self):
        return self.path


class Redirect(models.Model):
    """ریدایرکت آدرس‌های قدیمی وردپرس به آدرس‌های جدید."""
    old_path = models.CharField("مسیر قدیمی", max_length=300, unique=True, help_text="بدون دامنه. مثل /category/ai/")
    new_path = models.CharField("مسیر جدید", max_length=300, blank=True, help_text="خالی = ۴۱۰ (حذف شده)")
    status_code = models.PositiveSmallIntegerField("کد", choices=[(301, "301 دائمی"), (302, "302 موقت"), (410, "410 حذف شده")], default=301)
    hits = models.PositiveIntegerField("تعداد استفاده", default=0)
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        ordering = ["old_path"]
        verbose_name = "ریدایرکت"
        verbose_name_plural = "ریدایرکت‌ها"

    def __str__(self):
        return f"{self.old_path} → {self.new_path or '410'}"


class SEOFields(models.Model):
    """فیلدهای سئوی مشترک — به نوشته، محصول، دوره، صفحه و عضو تیم اضافه می‌شود."""
    seo_title = models.CharField("عنوان سئو", max_length=70, blank=True,
                                 help_text="عنوانی که در نتایج گوگل دیده می‌شود؛ ۵۰ تا ۶۰ کاراکتر. خالی = عنوان خود صفحه.")
    meta_description = models.CharField("توضیح متا", max_length=170, blank=True,
                                        help_text="متن زیر عنوان در گوگل؛ ۱۲۰ تا ۱۶۰ کاراکتر، با کلیدواژه و دعوت به کلیک.")
    focus_keyword = models.CharField("کلیدواژه‌ی کانونی", max_length=80, blank=True,
                                     help_text="عبارتی که می‌خواهید این صفحه با آن در گوگل پیدا شود. برای امتیاز سئو استفاده می‌شود.")
    canonical_url = models.URLField("آدرس کانونیکال", blank=True, help_text="فقط اگر همین محتوا جای دیگری هم منتشر شده؛ معمولاً خالی.")
    noindex = models.BooleanField("noindex", default=False, help_text="این صفحه در گوگل ایندکس نشود.")

    class Meta:
        abstract = True


class NotFoundLog(models.Model):
    """نمایشگر ۴۰۴ — آدرس‌هایی که بازدیدکننده یا ربات به آن‌ها رسیده و صفحه‌ای نبوده.
    با پر کردن «ریدایرکت به» یک ریدایرکت ۳۰۱ ساخته می‌شود."""
    path = models.CharField("مسیر", max_length=300, unique=True)
    hits = models.PositiveIntegerField("تعداد", default=1)
    referrer = models.CharField("آخرین ارجاع‌دهنده", max_length=300, blank=True)
    first_seen = models.DateTimeField("اولین بار", auto_now_add=True)
    last_seen = models.DateTimeField("آخرین بار", auto_now=True)
    redirect_to = models.CharField("ریدایرکت به", max_length=300, blank=True,
                                   help_text="مثلاً /blog/  — با ذخیره، ریدایرکت ۳۰۱ ساخته و این ردیف حل‌شده علامت می‌خورد.")
    resolved = models.BooleanField("حل شده", default=False)

    class Meta:
        ordering = ["resolved", "-hits"]
        verbose_name = "خطای ۴۰۴"
        verbose_name_plural = "نمایشگر ۴۰۴"

    def __str__(self):
        return self.path
