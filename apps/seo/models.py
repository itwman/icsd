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
