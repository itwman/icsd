"""تحلیل سئوی محتوا (مشابه Rank Math / Yoast) — همین قواعد در static/js/seo-panel.js زنده اجرا می‌شود."""
import re
from html import unescape

FA_NORMAL = str.maketrans({"ي": "ی", "ك": "ک", "‌": " ", "ة": "ه", "أ": "ا", "إ": "ا", "ۀ": "ه"})


def norm(s):
    return re.sub(r"\s+", " ", (s or "").translate(FA_NORMAL)).strip().lower()


def text_of(html):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", html or ""))).strip()


def analyze(*, title="", seo_title="", meta_description="", focus_keyword="", slug="", body="", site_name=""):
    """خروجی: (امتیاز ۰ تا ۱۰۰، فهرست (وضعیت، پیام)) — وضعیت: ok | warn | bad"""
    checks = []
    t = seo_title or title
    full_len = len(t) + (len(site_name) + 3 if site_name and not seo_title else 0)
    kw = norm(focus_keyword)
    text = text_of(body)
    words = len(text.split())
    add = lambda st, msg, w=1: checks.append((st, msg, w))

    if not kw:
        add("bad", "کلیدواژه‌ی کانونی تعیین نشده است.", 2)
    if 30 <= full_len <= 62:
        add("ok", f"طول عنوان مناسب است ({full_len} کاراکتر).")
    else:
        add("warn", f"طول عنوان {full_len} کاراکتر است؛ بهتر است بین ۳۰ تا ۶۰ باشد.")
    md = len(meta_description or "")
    if 110 <= md <= 165:
        add("ok", f"طول توضیح متا مناسب است ({md} کاراکتر).")
    elif md == 0:
        add("bad", "توضیح متا خالی است؛ گوگل خودش تکه‌ای از متن را انتخاب می‌کند.", 2)
    else:
        add("warn", f"توضیح متا {md} کاراکتر است؛ بهتر است ۱۲۰ تا ۱۶۰ باشد.")
    if kw:
        add("ok" if kw in norm(t) else "bad", "کلیدواژه در عنوان " + ("آمده است." if kw in norm(t) else "نیامده است."), 2)
        add("ok" if norm(t).startswith(kw) else "warn", "کلیدواژه " + ("در ابتدای عنوان است." if norm(t).startswith(kw) else "بهتر است در ابتدای عنوان بیاید."))
        add("ok" if kw in norm(meta_description) else "bad", "کلیدواژه در توضیح متا " + ("آمده است." if kw in norm(meta_description) else "نیامده است."))
        first = norm(" ".join(text.split()[:80]))
        add("ok" if kw in first else "warn", "کلیدواژه در پاراگراف اول " + ("آمده است." if kw in first else "نیامده است."))
        heads = norm(" ".join(re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body or "", re.S)))
        add("ok" if kw in heads else "warn", "کلیدواژه در تیترهای فرعی (H2/H3) " + ("آمده است." if kw in heads else "نیامده است."))
        n = norm(text).count(kw)
        density = (n * len(kw.split()) / words * 100) if words else 0
        if 0.5 <= density <= 2.5:
            add("ok", f"تراکم کلیدواژه مناسب است ({density:.1f}٪، {n} بار).")
        else:
            add("warn", f"تراکم کلیدواژه {density:.1f}٪ ({n} بار) است؛ بهتر است بین ۰٫۵ تا ۲٫۵ درصد باشد.")
        slug_n = norm(slug.replace("-", " "))
        if re.search(r"[؀-ۿ]", slug or ""):
            add("ok" if kw in slug_n else "warn", "نامک (آدرس) " + ("کلیدواژه را دارد." if kw in slug_n else "کلیدواژه را ندارد."))
    if body is not None and words:
        if words >= 600:
            add("ok", f"طول متن خوب است ({words} کلمه).")
        elif words >= 300:
            add("warn", f"متن {words} کلمه است؛ برای رقابت در گوگل ۶۰۰ کلمه به بالا بهتر است.")
        else:
            add("bad", f"متن کوتاه است ({words} کلمه).", 2)
        if "<h1" in (body or ""):
            add("bad", "داخل متن تیتر H1 هست؛ هر صفحه فقط یک H1 دارد (عنوان). از H2 استفاده کنید.")
        if re.search(r"<h2", body or ""):
            add("ok", "متن تیتر فرعی H2 دارد.")
        elif words >= 300:
            add("warn", "متن تیتر فرعی (H2) ندارد؛ ساختار تیتر به خوانایی و سئو کمک می‌کند.")
        imgs = re.findall(r"<img\b[^>]*>", body or "")
        no_alt = [i for i in imgs if not re.search(r'alt="[^"]+', i)]
        if imgs:
            add("ok" if not no_alt else "warn", "همه‌ی تصاویر متن جایگزین (alt) دارند." if not no_alt else f"{len(no_alt)} تصویر بدون متن جایگزین (alt).")
        links = re.findall(r'<a\b[^>]*href="([^"]+)"', body or "")
        internal = [l for l in links if l.startswith("/") or "icsd" in l]
        add("ok" if internal else "warn", "پیوند داخلی دارد." if internal else "پیوند داخلی ندارد؛ به یک صفحه‌ی مرتبط در سایت لینک دهید.")
    total = sum(w for _, _, w in checks) or 1
    got = sum(w if st == "ok" else (w * 0.5 if st == "warn" else 0) for st, _, w in checks)
    return round(got / total * 100), [(st, msg) for st, msg, _ in checks]


def analyze_obj(obj, body_field="body", title_field="title"):
    from apps.core.models import SiteSettings
    site = SiteSettings.load()
    return analyze(title=getattr(obj, title_field, "") or getattr(obj, "name", ""), seo_title=obj.seo_title,
                   meta_description=obj.meta_description, focus_keyword=obj.focus_keyword,
                   slug=getattr(obj, "slug", ""), body=getattr(obj, body_field, "") or "", site_name=site.site_name)
