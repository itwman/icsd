"""ابزارهای HTML محتوا: شناسه‌ی تیترها + فهرست مطالب، تخمین زمان مطالعه، تصویر lazy."""
import re
from html import unescape

from django.utils.text import slugify


def _text(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def add_heading_ids(html):
    """به H2/H3 شناسه می‌دهد (برای لینک مستقیم و فهرست مطالب) و فهرست را برمی‌گرداند:
    [{"id", "text", "level", "children": [...]}, ...]"""
    toc, used = [], set()

    def repl(m):
        level, attrs, inner = int(m.group(1)), m.group(2) or "", m.group(3)
        text = _text(inner)
        hid = re.search(r'id="([^"]+)"', attrs)
        hid = hid.group(1) if hid else (slugify(text, allow_unicode=True)[:60] or f"s{len(used) + 1}")
        base, n = hid, 2
        while hid in used:
            hid, n = f"{base}-{n}", n + 1
        used.add(hid)
        item = {"id": hid, "text": text, "level": level, "children": []}
        if level == 3 and toc:
            toc[-1]["children"].append(item)
        else:
            toc.append(item)
        attrs = re.sub(r'\s*id="[^"]*"', "", attrs)
        return f'<h{level}{attrs} id="{hid}">{inner}</h{level}>'

    out = re.sub(r"<h([23])(\s[^>]*)?>(.*?)</h\1>", repl, html or "", flags=re.S)
    return out, toc


def lazy_images(html):
    return re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy" decoding="async"', html or "")


def read_minutes(html, wpm=220):
    return max(1, round(len(_text(html or "").split()) / wpm))
