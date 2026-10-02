"""اعتبارسنجی لوگوها — PNG / WebP / SVG با اندازه‌ی استاندارد.

- محصول: مربع (۱:۱)، دست‌کم ۲۵۶ پیکسل، پیشنهاد ۵۱۲×۵۱۲ با پس‌زمینه‌ی شفاف، یا SVG مربع.
- مشتری: هر نسبتی (لوگوهای افقی رایج‌اند)، دست‌کم ۱۲۰ پیکسل در ضلع کوچک.
- SVG از نظر امنیتی بررسی می‌شود (script، on*=، javascript:، foreignObject ممنوع)؛
  چون فایل SVG اگر مستقیم باز شود می‌تواند کد اجرا کند.
"""
import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

LOGO_EXTS = ("png", "webp", "svg")
SVG_BAD = re.compile(rb"<\s*script|<\s*foreignObject|\son[a-z]+\s*=|javascript:|<!ENTITY|xlink:href\s*=\s*[\"']\s*(?:https?:|data:)", re.I)


def _svg_box(data: bytes):
    """ابعاد SVG از viewBox یا width/height (بدون نیاز به کتابخانه)."""
    head = data[:4000]
    m = re.search(rb'viewBox\s*=\s*["\']\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', head)
    if m:
        return float(m.group(1)), float(m.group(2))
    w = re.search(rb'\swidth\s*=\s*["\']([\d.]+)', head)
    h = re.search(rb'\sheight\s*=\s*["\']([\d.]+)', head)
    if w and h:
        return float(w.group(1)), float(h.group(1))
    return None


@deconstructible
class LogoValidator:
    def __init__(self, square=True, min_side=256, max_kb=800):
        self.square, self.min_side, self.max_kb = square, min_side, max_kb

    def __call__(self, f):
        name = (getattr(f, "name", "") or "").lower()
        ext = name.rsplit(".", 1)[-1] if "." in name else ""
        if ext not in LOGO_EXTS:
            raise ValidationError("فرمت لوگو باید PNG، WebP یا SVG باشد.")
        if f.size > self.max_kb * 1024:
            raise ValidationError(f"حجم لوگو حداکثر {self.max_kb} کیلوبایت باشد (این فایل {f.size // 1024} کیلوبایت است).")
        pos = f.tell() if hasattr(f, "tell") else 0
        f.seek(0)
        data = f.read()
        f.seek(pos)

        if ext == "svg":
            if b"<svg" not in data[:2000].lower():
                raise ValidationError("فایل SVG معتبر نیست.")
            if SVG_BAD.search(data):
                raise ValidationError("این SVG شامل اسکریپت یا پیوند خارجی است و به‌دلیل امنیت پذیرفته نمی‌شود. آن را از نرم‌افزار طراحی دوباره «Export» کنید.")
            box = _svg_box(data)
            if self.square and box and abs(box[0] / box[1] - 1) > 0.06:
                raise ValidationError("لوگوی محصول باید مربع باشد (viewBox با عرض و ارتفاع برابر).")
            return

        from io import BytesIO
        from PIL import Image
        try:
            im = Image.open(BytesIO(data))
            im.verify()
            im = Image.open(BytesIO(data))
        except Exception:
            raise ValidationError("فایل تصویر خراب یا نامعتبر است.")
        w, h = im.size
        if min(w, h) < self.min_side:
            raise ValidationError(f"اندازه‌ی لوگو دست‌کم {self.min_side} پیکسل باشد (این فایل {w}×{h} است). پیشنهاد: ۵۱۲×۵۱۲.")
        if self.square and abs(w / h - 1) > 0.06:
            raise ValidationError(f"لوگوی محصول باید مربع باشد؛ این فایل {w}×{h} است. پیشنهاد: ۵۱۲×۵۱۲ با پس‌زمینه‌ی شفاف.")

    def __eq__(self, other):
        return isinstance(other, LogoValidator) and (self.square, self.min_side, self.max_kb) == (other.square, other.min_side, other.max_kb)


validate_product_logo = LogoValidator(square=True, min_side=256, max_kb=800)
validate_customer_logo = LogoValidator(square=False, min_side=120, max_kb=800)

PRODUCT_LOGO_HELP = "مربع، PNG یا WebP با پس‌زمینه‌ی شفاف (پیشنهاد ۵۱۲×۵۱۲ پیکسل، حداقل ۲۵۶) یا SVG مربع. حداکثر ۸۰۰ کیلوبایت."
CUSTOMER_LOGO_HELP = "PNG یا WebP با پس‌زمینه‌ی شفاف (ارتفاع پیشنهادی ۲۰۰ پیکسل؛ لوگوی افقی هم مناسب است) یا SVG. حداکثر ۸۰۰ کیلوبایت."
