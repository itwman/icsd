from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.validators import PRODUCT_LOGO_HELP, validate_product_logo


class Product(models.Model):
    STATUS = [("stable", "پایدار"), ("beta", "بتا"), ("alpha", "آلفا"), ("dev", "در حال توسعه")]

    name = models.CharField("نام محصول", max_length=100)
    slug = models.SlugField("نامک (در آدرس)", unique=True, allow_unicode=True)
    latin_name = models.CharField("نام لاتین", max_length=60, blank=True)
    tagline = models.CharField("شعار یک‌خطی", max_length=200)
    category_label = models.CharField("برچسب دسته (مثل MES · IoT)", max_length=60, blank=True)
    color = models.CharField("رنگ اختصاصی", max_length=7, default="#1E9E7B")
    icon = models.CharField("آیکن (نام Material)", max_length=40, default="memory")
    cover = models.ImageField("تصویر اصلی", upload_to="products/", blank=True)
    logo = models.FileField("لوگوی محصول", upload_to="products/logos/", blank=True,
                            validators=[validate_product_logo], help_text=PRODUCT_LOGO_HELP)
    status = models.CharField("وضعیت", max_length=10, choices=STATUS, default="stable")
    version = models.CharField("نسخه", max_length=20, blank=True, help_text="مثل 3.5 (بدون v)")
    license_label = models.CharField("مجوز", max_length=40, blank=True, help_text="مثل: تجاری، رایگان، متن‌باز")

    summary = models.TextField("خلاصه", blank=True)
    description = CKEditor5Field("شرح کامل", config_name="default", blank=True)
    target_audience = models.TextField("برای چه کسانی", blank=True)
    tech_stack = models.CharField("فناوری‌ها", max_length=200, blank=True, help_text="مثل: Django, PostgreSQL, React")

    catalog_pdf = models.FileField("کاتالوگ PDF (اختیاری)", upload_to="products/catalogs/", blank=True,
                                   help_text="اگر خالی باشد، صفحه‌ی کاتالوگ خودکار از همین اطلاعات ساخته می‌شود.")
    demo_url = models.URLField("لینک دمو", blank=True)
    price_note = models.CharField("یادداشت قیمت", max_length=120, blank=True, default="قیمت بر اساس نیاز مشتری")

    related_courses = models.ManyToManyField("academy.Course", verbose_name="دوره‌های مرتبط", blank=True, related_name="products")

    is_active = models.BooleanField("فعال", default=True)
    is_featured = models.BooleanField("نمایش در صفحه اصلی", default=False,
                                      help_text="محصولات علامت‌خورده در بخش «محصولات» صفحه‌ی اصلی می‌آیند (به ترتیب).")
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", args=[self.slug])

    @property
    def tech_list(self):
        return [t.strip() for t in (self.tech_stack or "").split(",") if t.strip()]


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="features")
    title = models.CharField("عنوان قابلیت", max_length=120)
    text = models.TextField("توضیح", blank=True)
    icon = models.CharField("آیکن", max_length=40, blank=True, default="check_circle")
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "قابلیت"
        verbose_name_plural = "قابلیت‌ها"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("تصویر", upload_to="products/gallery/")
    caption = models.CharField("زیرنویس", max_length=150, blank=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "تصویر محصول"
        verbose_name_plural = "گالری"


class ProductTutorial(models.Model):
    """آموزش‌های اختصاصی هر محصول — متن، ویدیو یا پیوند به یک دوره."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="tutorials")
    title = models.CharField("عنوان آموزش", max_length=150)
    body = CKEditor5Field("متن", config_name="default", blank=True)
    embed_html = models.TextField("کد ویدیو (اختیاری)", blank=True)
    attachment = models.FileField("فایل", upload_to="products/tutorials/", blank=True)
    course = models.ForeignKey("academy.Course", verbose_name="یا پیوند به دوره", null=True, blank=True, on_delete=models.SET_NULL)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    is_public = models.BooleanField("عمومی (بدون ورود)", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "آموزش محصول"
        verbose_name_plural = "آموزش‌های محصول"

    def __str__(self):
        return self.title
