"""فیلترها و تگ‌های فارسی: تاریخ شمسی، ارقام فارسی، مبلغ، دکمه‌ی ویرایش برای مدیر."""
from datetime import date, datetime

import jdatetime
from django import template
from django.contrib.contenttypes.models import ContentType
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.html import format_html

register = template.Library()

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
EN_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")

JMONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
           "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
JWEEKDAYS = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]


def _to_j(value):
    if isinstance(value, datetime):
        if timezone.is_aware(value):
            value = timezone.localtime(value)
        return jdatetime.datetime.fromgregorian(datetime=value)
    if isinstance(value, date):
        return jdatetime.date.fromgregorian(date=value)
    return None


@register.filter
def jdate(value, fmt="%Y/%m/%d"):
    """تاریخ شمسی با ارقام فارسی. نمونه: {{ obj.created|jdate:"%d %B %Y" }}"""
    j = _to_j(value)
    if j is None:
        return ""
    out = j.strftime(fmt)
    # نام ماه و روز هفته را فارسی کن (jdatetime به انگلیسی برمی‌گرداند)
    for i, en in enumerate(["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar",
                            "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]):
        out = out.replace(en, JMONTHS[i])
    for i, en in enumerate(["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]):
        out = out.replace(en, JWEEKDAYS[i])
    return out.translate(FA_DIGITS)


@register.filter
def jdatetime_fa(value):
    """تاریخ و ساعت شمسی: ۱۴۰۵/۰۶/۲۲ - ۱۴:۳۰"""
    j = _to_j(value)
    if j is None:
        return ""
    return j.strftime("%Y/%m/%d - %H:%M").translate(FA_DIGITS)


@register.filter
def fa_num(value):
    return str(value).translate(FA_DIGITS)


@register.filter
def en_num(value):
    return str(value).translate(EN_DIGITS)


@register.filter
def toman(value):
    """۱٬۲۰۰٬۰۰۰ تومان — صفر یعنی رایگان"""
    try:
        n = int(value)
    except (TypeError, ValueError):
        return ""
    if n == 0:
        return "رایگان"
    return f"{n:,}".replace(",", "٬").translate(FA_DIGITS) + " تومان"


@register.filter
def minutes_fa(total):
    """۶۰۰ دقیقه → ۱۰ ساعت"""
    try:
        m = int(total)
    except (TypeError, ValueError):
        return ""
    h, r = divmod(m, 60)
    if h and r:
        return f"{h} ساعت و {r} دقیقه".translate(FA_DIGITS)
    if h:
        return f"{h} ساعت".translate(FA_DIGITS)
    return f"{r} دقیقه".translate(FA_DIGITS)


@register.filter
def highlight(text, part):
    """بخشی از تیتر را با <span class="g"> رنگی می‌کند."""
    from django.utils.html import escape
    from django.utils.safestring import mark_safe
    text = escape(text or "")
    part = escape(part or "")
    if part and part in text:
        text = text.replace(part, f'<span class="g">{part}</span>', 1)
    return mark_safe(text)


@register.simple_tag
def jyear():
    """سال شمسی جاری با ارقام فارسی"""
    return str(jdatetime.date.today().year).translate(FA_DIGITS)


@register.simple_tag
def jtoday(fmt="%d %B %Y"):
    return jdate(jdatetime.date.today().togregorian(), fmt)


@register.simple_tag(takes_context=True)
def edit_btn(context, obj, label="ویرایش"):
    """
    دکمه‌ی «ویرایش» کنار هر بخش — فقط برای کاربر staff که مجوز تغییر آن مدل را دارد.
    استفاده: {% edit_btn course %}
    """
    request = context.get("request")
    user = getattr(request, "user", None)
    if not obj or not user or not user.is_staff:
        return ""
    ct = ContentType.objects.get_for_model(obj.__class__)
    perm = f"{ct.app_label}.change_{ct.model}"
    if not user.has_perm(perm):
        return ""
    try:
        url = reverse(f"admin:{ct.app_label}_{ct.model}_change", args=[obj.pk])
    except NoReverseMatch:
        return ""
    return format_html(
        '<a class="edit-btn" href="{}" target="_blank" rel="noopener" title="ویرایش در پنل مدیریت">'
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>{}</a>',
        url, label,
    )


@register.simple_tag(takes_context=True)
def add_btn(context, app_label, model, label="افزودن"):
    """دکمه‌ی «افزودن» برای فهرست‌ها. استفاده: {% add_btn "academy" "course" %}"""
    request = context.get("request")
    user = getattr(request, "user", None)
    if not user or not user.is_staff or not user.has_perm(f"{app_label}.add_{model}"):
        return ""
    try:
        url = reverse(f"admin:{app_label}_{model}_add")
    except NoReverseMatch:
        return ""
    return format_html('<a class="edit-btn edit-btn--add" href="{}" target="_blank" rel="noopener">+ {}</a>', url, label)
