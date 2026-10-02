"""میکسین‌های پنل مدیریت: تقویم شمسی روی همه‌ی فیلدهای تاریخ."""
from django.db import models

from .forms import JalaliDateField, JalaliDateWidget

try:
    from unfold.widgets import INPUT_CLASSES
    _ADMIN_INPUT = " ".join(INPUT_CLASSES) + " jdp"
except Exception:  # اگر نسخه‌ی unfold این ثابت را نداشت
    _ADMIN_INPUT = "vTextField jdp"


class JalaliAdminMixin:
    """
    هر DateField در فرم ادمین با تقویم شمسی نمایش داده می‌شود.
    DateTimeField را دست نمی‌زنیم (auto_now معمولاً readonly است).
    """

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, models.DateField) and not isinstance(db_field, models.DateTimeField):
            kwargs["form_class"] = JalaliDateField
            kwargs["widget"] = JalaliDateWidget(attrs={"class": _ADMIN_INPUT},
                                                birth=(db_field.name in ("birth_date", "birthday")))
            kwargs.pop("localize", None)
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)
