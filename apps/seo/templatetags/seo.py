"""
{% seo_head seo_obj %} — عنوان، توضیح، OG و کانونیکال را می‌سازد.
اولویت: رکورد SEOMeta برای این مسیر → فیلدهای آبجکت → پیش‌فرض تنظیمات سایت.
"""
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from apps.seo.models import SEOMeta

register = template.Library()


@register.simple_tag(takes_context=True)
def seo_head(context, obj=None, title=None, description=None):
    request = context["request"]
    site = context.get("site")
    meta = SEOMeta.objects.filter(path=request.path).first()

    t = (meta and meta.title) or title or getattr(obj, "seo_title", None) or getattr(obj, "title", None) or getattr(obj, "name", None) or ""
    d = (meta and meta.description) or description or getattr(obj, "summary", None) or getattr(obj, "excerpt", None) or getattr(obj, "tagline", None) or (site.default_meta_description if site else "")
    full_title = f"{t} | {site.site_name}" if t and site else (site.site_name if site else t)

    img = None
    if meta and meta.og_image:
        img = meta.og_image.url
    elif getattr(obj, "cover", None):
        img = obj.cover.url
    elif site and site.default_og_image:
        img = site.default_og_image.url
    if img and not img.startswith("http"):
        img = request.build_absolute_uri(img)

    canonical = (meta and meta.canonical) or request.build_absolute_uri(request.path)
    html = f"<title>{escape(full_title)}</title>\n"
    html += f'<meta name="description" content="{escape(d[:300])}">\n'
    if meta and meta.keywords:
        html += f'<meta name="keywords" content="{escape(meta.keywords)}">\n'
    if meta and meta.noindex:
        html += '<meta name="robots" content="noindex,follow">\n'
    html += f'<link rel="canonical" href="{escape(canonical)}">\n'
    html += f'<meta property="og:title" content="{escape(full_title)}">\n'
    html += f'<meta property="og:description" content="{escape(d[:300])}">\n'
    html += f'<meta property="og:url" content="{escape(canonical)}">\n'
    html += '<meta property="og:type" content="website">\n'
    if site:
        html += f'<meta property="og:site_name" content="{escape(site.site_name)}">\n'
    if img:
        html += f'<meta property="og:image" content="{escape(img)}">\n<meta name="twitter:card" content="summary_large_image">\n'
    if meta and meta.schema_json.strip():
        html += f'<script type="application/ld+json">{meta.schema_json}</script>\n'
    return mark_safe(html)
