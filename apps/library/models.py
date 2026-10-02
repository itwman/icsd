import os

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from apps.seo.models import SEOFields


class BookCategory(models.Model):
    title = models.CharField("عنوان", max_length=80, unique=True)
    slug = models.SlugField("نامک", max_length=100, unique=True, allow_unicode=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "دسته‌بندی کتاب"
        verbose_name_plural = "دسته‌بندی کتاب‌ها"

    def __str__(self):
        return self.title


class Book(SEOFields, models.Model):
    KINDS = [("authored", "تألیف"), ("translated", "ترجمه"), ("compiled", "گردآوری"), ("other", "سایر")]
    FORMATS = [("pdf", "PDF"), ("epub", "EPUB"), ("zip", "ZIP"), ("other", "سایر")]

    title = models.CharField("عنوان کتاب", max_length=200)
    slug = models.SlugField("نامک (در آدرس)", max_length=200, unique=True, allow_unicode=True)
    subtitle = models.CharField("زیرعنوان", max_length=250, blank=True)
    category = models.ForeignKey(BookCategory, verbose_name="دسته‌بندی", null=True, blank=True, on_delete=models.SET_NULL, related_name="books")
    kind = models.CharField("نوع اثر", max_length=12, choices=KINDS, default="authored")
    authors = models.CharField("نویسنده(ها)", max_length=200, blank=True)
    translator = models.CharField("مترجم", max_length=200, blank=True)
    publisher = models.CharField("ناشر", max_length=150, blank=True)
    year = models.CharField("سال انتشار", max_length=10, blank=True, help_text="مثل ۱۴۰۵")
    edition = models.CharField("نوبت چاپ", max_length=30, blank=True)
    pages = models.PositiveIntegerField("تعداد صفحات", null=True, blank=True)
    language = models.CharField("زبان", max_length=30, default="فارسی")
    isbn = models.CharField("شابک", max_length=30, blank=True)

    cover = models.ImageField("جلد", upload_to="library/covers/", blank=True, help_text="عمودی، پیشنهاد ۶۰۰×۸۴۸ پیکسل.")
    cover_alt = models.CharField("متن جایگزین جلد", max_length=200, blank=True)
    excerpt = models.TextField("معرفی کوتاه", blank=True, help_text="۱ تا ۳ جمله؛ در کارت کتاب و توضیح متا.")
    description = CKEditor5Field("معرفی کامل", config_name="default", blank=True)

    file = models.FileField("فایل کتاب", upload_to="library/files/", blank=True,
                            validators=[FileExtensionValidator(["pdf", "epub", "zip"])],
                            help_text="PDF، EPUB یا ZIP. اگر فایل روی سرور دیگری است، به‌جای آن «لینک دانلود» را پر کنید.")
    download_url = models.URLField("لینک دانلود بیرونی", max_length=500, blank=True)
    preview_url = models.URLField("لینک پیش‌نمایش / مطالعه‌ی آنلاین", max_length=500, blank=True)
    file_format = models.CharField("قالب فایل", max_length=8, choices=FORMATS, default="pdf")
    file_size = models.CharField("حجم فایل", max_length=20, blank=True, help_text="خالی = خودکار از فایل آپلودی")
    require_login = models.BooleanField("دانلود فقط برای کاربران وارد شده", default=False)

    download_count = models.PositiveIntegerField("تعداد دانلود", default=0)
    view_count = models.PositiveIntegerField("تعداد بازدید", default=0)
    is_featured = models.BooleanField("ویژه (صفحه اصلی)", default=False)
    is_published = models.BooleanField("منتشر شده", default=True)
    order = models.PositiveSmallIntegerField("ترتیب", default=0)
    published_at = models.DateField("تاریخ انتشار", null=True, blank=True)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        ordering = ["order", "-published_at", "-id"]
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("library:detail", args=[self.slug])

    def get_download_url(self):
        return reverse("library:download", args=[self.slug])

    @property
    def has_download(self):
        return bool(self.file or self.download_url)

    @property
    def size_label(self):
        if self.file_size:
            return self.file_size
        if self.file:
            try:
                n = self.file.size
            except (OSError, ValueError):
                return ""
            return f"{n / 1048576:.1f} MB" if n >= 1048576 else f"{max(1, n // 1024)} KB"
        return ""

    @property
    def body(self):
        """برای پنل سئو و تحلیل محتوا."""
        return self.description or self.excerpt

    def save(self, *args, **kwargs):
        if self.file and not self.download_url:
            ext = os.path.splitext(self.file.name)[1].lower().lstrip(".")
            if ext in dict(self.FORMATS):
                self.file_format = ext
        super().save(*args, **kwargs)
