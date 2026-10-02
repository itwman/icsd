from django.conf import settings
from django.db import models


class Order(models.Model):
    STATUS = [("pending", "در انتظار پرداخت"), ("paid", "پرداخت شده"), ("failed", "ناموفق"), ("canceled", "لغو شده")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.PROTECT, related_name="orders")
    course = models.ForeignKey("academy.Course", verbose_name="دوره", on_delete=models.PROTECT, related_name="orders")
    amount = models.PositiveIntegerField("مبلغ (تومان)")
    status = models.CharField("وضعیت", max_length=10, choices=STATUS, default="pending")
    gateway = models.CharField("درگاه", max_length=20, default="zarinpal")
    authority = models.CharField("Authority", max_length=64, blank=True, db_index=True)
    ref_id = models.CharField("کد پیگیری", max_length=64, blank=True)
    card_pan = models.CharField("شماره کارت (ماسک)", max_length=24, blank=True)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    paid_at = models.DateTimeField("زمان پرداخت", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"

    def __str__(self):
        return f"#{self.pk} {self.user} — {self.course} ({self.get_status_display()})"
