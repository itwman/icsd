from django.conf import settings
from django.db import models


class Province(models.Model):
    name = models.CharField("استان", max_length=60, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "استان"
        verbose_name_plural = "استان‌ها"

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, verbose_name="استان", on_delete=models.CASCADE, related_name="cities")
    name = models.CharField("شهر", max_length=80)

    class Meta:
        ordering = ["name"]
        unique_together = [("province", "name")]
        verbose_name = "شهر"
        verbose_name_plural = "شهرها"

    def __str__(self):
        return self.name


class ProjectRequest(models.Model):
    """درخواست شروع پروژه — با مشخصات کامل مشتری و آدرس."""
    STATUS = [("new", "جدید"), ("contacted", "تماس گرفته شد"), ("meeting", "جلسه"),
              ("proposal", "پیشنهاد ارسال شد"), ("won", "قرارداد بسته شد"), ("lost", "منتفی")]
    TOPICS = [("mes", "اتوماسیون خط تولید / MES"), ("erp", "ERP و برنامه‌ریزی"), ("cmms", "نگهداری و تعمیرات"),
              ("web", "وب‌سایت / فروشگاه"), ("app", "اپلیکیشن موبایل"), ("ai", "هوش مصنوعی / تحلیل داده"),
              ("training", "آموزش سازمانی"), ("other", "سایر")]
    BUDGETS = [("", "مشخص نیست"), ("lt50", "کمتر از ۵۰ میلیون"), ("50-150", "۵۰ تا ۱۵۰ میلیون"),
               ("150-500", "۱۵۰ تا ۵۰۰ میلیون"), ("gt500", "بیش از ۵۰۰ میلیون")]

    # مشتری
    full_name = models.CharField("نام و نام خانوادگی", max_length=120)
    company = models.CharField("نام شرکت / کارخانه", max_length=150, blank=True)
    job_title = models.CharField("سمت", max_length=80, blank=True)
    mobile = models.CharField("موبایل", max_length=11)
    phone = models.CharField("تلفن ثابت", max_length=20, blank=True)
    email = models.EmailField("ایمیل", blank=True)

    # آدرس
    province = models.ForeignKey(Province, verbose_name="استان", null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, verbose_name="شهر", null=True, blank=True, on_delete=models.SET_NULL)
    address = models.TextField("آدرس", blank=True)
    postal_code = models.CharField("کد پستی", max_length=10, blank=True)

    # پروژه
    topic = models.CharField("موضوع", max_length=12, choices=TOPICS, default="other")
    product = models.ForeignKey("products.Product", verbose_name="محصول مورد نظر", null=True, blank=True, on_delete=models.SET_NULL)
    budget = models.CharField("بودجه‌ی تقریبی", max_length=10, choices=BUDGETS, blank=True)
    preferred_date = models.DateField("تاریخ مناسب برای جلسه", null=True, blank=True)
    description = models.TextField("شرح نیاز")
    attachment = models.FileField("فایل پیوست", upload_to="leads/", blank=True)

    # پیگیری
    status = models.CharField("وضعیت", max_length=12, choices=STATUS, default="new")
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="مسئول پیگیری", null=True, blank=True,
                                    on_delete=models.SET_NULL, related_name="assigned_leads")
    notes = models.TextField("یادداشت داخلی", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="project_requests", editable=False)
    created_at = models.DateTimeField("تاریخ ثبت", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "درخواست پروژه"
        verbose_name_plural = "درخواست‌های پروژه"

    def __str__(self):
        return f"{self.full_name} — {self.get_topic_display()}"
