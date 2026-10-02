from django.conf import settings
from django.db import models


class PageView(models.Model):
    path = models.CharField("مسیر", max_length=300, db_index=True)
    title = models.CharField("عنوان", max_length=200, blank=True)
    referrer = models.CharField("ارجاع‌دهنده", max_length=300, blank=True)
    user_agent = models.CharField("مرورگر", max_length=300, blank=True)
    device = models.CharField("دستگاه", max_length=10, blank=True)  # mobile / desktop / bot
    ip_hash = models.CharField("هش IP", max_length=64, blank=True, db_index=True)
    session_key = models.CharField(max_length=40, blank=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField("زمان", auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "بازدید صفحه"
        verbose_name_plural = "بازدیدها"

    def __str__(self):
        return f"{self.path} @ {self.created_at:%Y-%m-%d %H:%M}"
