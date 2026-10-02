"""فیلد و ویجت تاریخ شمسی برای فرم‌ها و پنل مدیریت."""
import jdatetime
from django import forms

EN = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


class JalaliDateWidget(forms.TextInput):
    """ورودی متنی که jalalidatepicker روی آن سوار می‌شود."""

    def __init__(self, attrs=None, birth=False):
        base = {
            "data-jdp": "",
            "data-jdp-only-date": "",
            "autocomplete": "off",
            "class": "form-control jdp",
            "placeholder": "۱۴۰۵/۰۶/۲۲",
            "dir": "ltr",
        }
        if birth:
            base.update({"data-jdp-min-date": "1300/01/01", "data-jdp-max-date": "today"})
        if attrs:
            base.update(attrs)
        super().__init__(base)

    def format_value(self, value):
        if not value:
            return ""
        if isinstance(value, str):
            return value
        j = jdatetime.date.fromgregorian(date=value)
        return j.strftime("%Y/%m/%d").translate(FA)


class JalaliDateField(forms.Field):
    widget = JalaliDateWidget
    default_error_messages = {"invalid": "تاریخ نامعتبر است. نمونه: ۱۴۰۵/۰۶/۲۲"}

    def to_python(self, value):
        if value in self.empty_values:
            return None
        if not isinstance(value, str):
            return value
        v = value.strip().translate(EN).replace("-", "/").replace(".", "/")
        try:
            y, m, d = (int(p) for p in v.split("/"))
            return jdatetime.date(y, m, d).togregorian()
        except (ValueError, TypeError):
            raise forms.ValidationError(self.error_messages["invalid"], code="invalid")

    def prepare_value(self, value):
        return value


def normalize_digits(value: str) -> str:
    """ارقام فارسی/عربی → لاتین (برای موبایل، کدپستی و ...)"""
    return (value or "").translate(EN)
