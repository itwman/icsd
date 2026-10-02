from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from apps.seo.models import SEOFields


class Tag(models.Model):
    name = models.CharField("نام", max_length=60, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب‌ها"

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    title = models.CharField("عنوان", max_length=80, unique=True)
    slug = models.SlugField("نامک", unique=True, allow_unicode=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "دسته‌بندی نوشته"
        verbose_name_plural = "دسته‌بندی نوشته‌ها"

    def __str__(self):
        return self.title


class Post(SEOFields, models.Model):
    title = models.CharField("عنوان", max_length=200)
    slug = models.SlugField("نامک (در آدرس)", unique=True, allow_unicode=True,
                            help_text="ترجیحاً انگلیسی — مثل tarahi-site-farsh-kashan")
    category = models.ForeignKey(BlogCategory, verbose_name="دسته‌بندی", on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag, verbose_name="برچسب‌ها", blank=True, related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="نویسنده", null=True, blank=True,
                               on_delete=models.SET_NULL, related_name="posts")
    excerpt = models.CharField("خلاصه", max_length=300, blank=True)
    body = CKEditor5Field("متن", config_name="default")
    cover = models.ImageField("تصویر شاخص", upload_to="blog/", blank=True,
                              help_text="پیشنهاد: ۱۲۰۰×۶۳۰ پیکسل (نسبت شبکه‌های اجتماعی)، JPG یا WebP زیر ۲۰۰ کیلوبایت.")
    cover_alt = models.CharField("متن جایگزین تصویر شاخص", max_length=200, blank=True, help_text="برای نابینایان و گوگل؛ خالی = عنوان نوشته.")
    read_minutes = models.PositiveSmallIntegerField("زمان مطالعه (دقیقه)", default=5)
    is_published = models.BooleanField("منتشر شده", default=True)
    published_at = models.DateTimeField("تاریخ انتشار", default=timezone.now)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)
    views = models.PositiveIntegerField("بازدید", default=0)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "نوشته"
        verbose_name_plural = "نوشته‌ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])
