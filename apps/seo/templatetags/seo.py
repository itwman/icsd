"""
تگ‌های سئو:
  {% seo_head obj "عنوان" "توضیح" %}  — title، description، robots، canonical، OG، Twitter، JSON-LD
  {% breadcrumbs obj %}               — مسیر راهنما (نمایشی + BreadcrumbList)

اولویت: رکورد SEOMeta همان مسیر → فیلدهای سئوی آبجکت (seo_title، meta_description، noindex، canonical_url)
→ آرگومان‌های تگ → عنوان/خلاصه‌ی آبجکت → پیش‌فرض تنظیمات سایت.
"""
import json
import re
from html import unescape

from django import template
from django.urls import reverse
from django.utils.html import escape, format_html_join
from django.utils.safestring import mark_safe

from apps.seo.models import SEOMeta

register = template.Library()


def _plain(s, n=None):
    s = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", str(s or "")))).strip()
    if n and len(s) > n:
        s = s[: n - 1].rsplit(" ", 1)[0] + "…"
    return s


def _abs(request, url):
    if not url:
        return ""
    return url if url.startswith("http") else request.build_absolute_uri(url)


def _img(obj):
    for f in ("cover", "photo", "logo", "image"):
        v = getattr(obj, f, None)
        if v:
            try:
                return v.url
            except ValueError:
                pass
    return None


def _ld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"


def _org(site, request):
    base = site.site_url.rstrip("/")
    logo = _abs(request, site.logo.url) if site.logo else base + "/static/img/logo.svg"
    same = [u for u in (site.instagram, site.telegram, site.linkedin, site.aparat) if u]
    org = {"@type": "Organization", "@id": base + "/#org", "name": site.site_name, "url": base + "/", "logo": logo}
    if same:
        org["sameAs"] = same
    if site.phone:
        org["contactPoint"] = {"@type": "ContactPoint", "telephone": site.phone, "contactType": "customer service",
                               "areaServed": "IR", "availableLanguage": "fa"}
    if site.address:
        org["address"] = {"@type": "PostalAddress", "streetAddress": site.address, "addressCountry": "IR"}
    return org


def _schema(obj, request, site, title, desc, img):
    """JSON-LD مناسب هر نوع آبجکت."""
    base = site.site_url.rstrip("/")
    url = request.build_absolute_uri(request.path)
    name = obj.__class__.__name__
    if name == "Post":
        d = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": obj.title[:110], "description": desc,
             "datePublished": obj.published_at.isoformat(), "dateModified": obj.updated_at.isoformat(),
             "mainEntityOfPage": url, "inLanguage": "fa-IR", "publisher": {"@id": base + "/#org"},
             "author": {"@type": "Organization", "name": site.site_name, "url": base + "/"}}
        if obj.author_id:
            d["author"] = {"@type": "Person", "name": obj.author.get_full_name() or site.site_name}
        if img:
            d["image"] = [img]
        if obj.category_id:
            d["articleSection"] = obj.category.title
        kws = [t.name for t in obj.tags.all()]
        if obj.focus_keyword:
            kws.insert(0, obj.focus_keyword)
        if kws:
            d["keywords"] = ", ".join(kws)
        d["wordCount"] = len(_plain(obj.body).split())
        return d
    if name == "Product":
        d = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": obj.name, "description": desc, "url": url,
             "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
             "publisher": {"@id": base + "/#org"}, "inLanguage": "fa-IR"}
        if obj.version:
            d["softwareVersion"] = obj.version
        if img:
            d["image"] = img
        if obj.price_note and "رایگان" in obj.price_note:
            d["offers"] = {"@type": "Offer", "price": "0", "priceCurrency": "IRR"}
        return d
    if name == "Course":
        d = {"@context": "https://schema.org", "@type": "Course", "name": obj.title, "description": desc, "url": url,
             "inLanguage": "fa-IR", "isAccessibleForFree": True,
             "provider": {"@type": "Organization", "name": site.site_name, "sameAs": base + "/"},
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "IRR", "category": "Free"},
             "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online",
                                   "courseWorkload": f"PT{obj.duration_minutes or 60}M"}}
        if img:
            d["image"] = img
        return d
    if name == "TeamMember":
        p = {"@type": "Person", "name": obj.name, "jobTitle": obj.role, "description": desc, "url": url,
             "worksFor": {"@id": base + "/#org"}}
        if obj.name_en:
            p["alternateName"] = obj.name_en
        if img:
            p["image"] = img
        same = [s.url for s in obj.socials.all()]
        if same:
            p["sameAs"] = same
        alumni = [{"@type": "EducationalOrganization", "name": e.org} for e in obj.education.all() if e.org]
        if alumni:
            p["alumniOf"] = alumni
        skills = [s.name for s in obj.skills.all()]
        if skills:
            p["knowsAbout"] = skills
        return {"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": p, "url": url}
    if name == "Book":
        d = {"@context": "https://schema.org", "@type": "Book", "name": obj.title, "description": desc, "url": url,
             "inLanguage": "fa-IR" if (obj.language or "فارسی") == "فارسی" else obj.language,
             "publisher": {"@type": "Organization", "name": obj.publisher or site.site_name},
             "isAccessibleForFree": True}
        if obj.authors:
            d["author"] = [{"@type": "Person", "name": a.strip()} for a in re.split(r"[،,]", obj.authors) if a.strip()]
        if obj.translator:
            d["translator"] = {"@type": "Person", "name": obj.translator}
        if obj.pages:
            d["numberOfPages"] = obj.pages
        if obj.isbn:
            d["isbn"] = obj.isbn
        if img:
            d["image"] = img
        if obj.published_at:
            d["datePublished"] = obj.published_at.isoformat()
        if obj.has_download:
            d["bookFormat"] = "https://schema.org/EBook"
            d["offers"] = {"@type": "Offer", "price": "0", "priceCurrency": "IRR", "availability": "https://schema.org/InStock"}
        return d
    if name == "Game":
        return {"@context": "https://schema.org", "@type": "VideoGame", "name": obj.title, "description": desc, "url": url,
                "inLanguage": "fa-IR", "gamePlatform": "Web browser", "applicationCategory": "Game",
                "operatingSystem": "Web", "publisher": {"@id": base + "/#org"},
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "IRR"}}
    if name == "Page":
        return {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "fa-IR"}
    return None


@register.simple_tag(takes_context=True)
def seo_head(context, obj=None, title=None, description=None):
    request = context["request"]
    site = context.get("site")
    meta = SEOMeta.objects.filter(path=request.path).first()
    site_name = site.site_name if site else ""

    custom_title = (meta and meta.title) or getattr(obj, "seo_title", "") or ""
    t = custom_title or title or getattr(obj, "title", None) or getattr(obj, "name", None) or ""
    full_title = custom_title or (f"{t} | {site_name}" if t and site_name and t != site_name else (t or site_name))
    d = ((meta and meta.description) or getattr(obj, "meta_description", "") or description
         or getattr(obj, "excerpt", None) or getattr(obj, "summary", None) or getattr(obj, "tagline", None)
         or _plain(getattr(obj, "body", "") or getattr(obj, "about", "") or getattr(obj, "description", ""), 160)
         or (site.default_meta_description if site else ""))
    d = _plain(d, 165)

    img = (meta and meta.og_image and meta.og_image.url) or _img(obj) or (site.default_og_image.url if site and site.default_og_image else None)
    img = _abs(request, img) if img else (site.site_url.rstrip("/") + "/static/img/logo.svg" if site else "")

    private = request.path.startswith(("/accounts/", "/pay/", "/verify/")) or "/quiz/" in request.path
    noindex = (meta and meta.noindex) or getattr(obj, "noindex", False) or private or request.GET.get("q")
    canonical = (meta and meta.canonical) or getattr(obj, "canonical_url", "") or request.build_absolute_uri(request.path)
    is_article = obj is not None and obj.__class__.__name__ == "Post"

    h = [f"<title>{escape(full_title)}</title>",
         f'<meta name="description" content="{escape(d)}">',
         '<meta name="robots" content="noindex, follow">' if noindex else
         '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
         f'<link rel="canonical" href="{escape(canonical)}">',
         f'<link rel="alternate" hreflang="fa-IR" href="{escape(canonical)}">',
         '<meta property="og:locale" content="fa_IR">',
         f'<meta property="og:type" content="{"article" if is_article else "website"}">',
         f'<meta property="og:title" content="{escape(full_title)}">',
         f'<meta property="og:description" content="{escape(d)}">',
         f'<meta property="og:url" content="{escape(canonical)}">',
         f'<meta property="og:site_name" content="{escape(site_name)}">',
         '<meta name="twitter:card" content="summary_large_image">',
         f'<meta name="twitter:title" content="{escape(full_title)}">',
         f'<meta name="twitter:description" content="{escape(d)}">']
    if img:
        h += [f'<meta property="og:image" content="{escape(img)}">', f'<meta property="og:image:alt" content="{escape(t)}">',
              f'<meta name="twitter:image" content="{escape(img)}">']
    if is_article:
        h += [f'<meta property="article:published_time" content="{obj.published_at.isoformat()}">',
              f'<meta property="article:modified_time" content="{obj.updated_at.isoformat()}">']
        if obj.category_id:
            h.append(f'<meta property="article:section" content="{escape(obj.category.title)}">')
        h += [f'<meta property="article:tag" content="{escape(tg.name)}">' for tg in obj.tags.all()]
    if meta and meta.keywords:
        h.append(f'<meta name="keywords" content="{escape(meta.keywords)}">')
    out = "\n".join(h) + "\n"

    if site:
        graph = [_org(site, request)]
        if request.path == "/":
            base = site.site_url.rstrip("/")
            graph.append({"@type": "WebSite", "@id": base + "/#website", "url": base + "/", "name": site_name,
                          "inLanguage": "fa-IR", "publisher": {"@id": base + "/#org"},
                          "potentialAction": {"@type": "SearchAction", "target": base + "/blog/?q={search_term_string}",
                                              "query-input": "required name=search_term_string"}})
        out += _ld({"@context": "https://schema.org", "@graph": graph})
    if obj is not None and site:
        sc = _schema(obj, request, site, t, d, img)
        if sc:
            out += _ld(sc)
    if meta and meta.schema_json.strip():
        out += f'<script type="application/ld+json">{meta.schema_json}</script>\n'
    return mark_safe(out)


def _crumbs(obj):
    home = ("خانه", "/")
    name = obj.__class__.__name__ if obj is not None else ""
    if name == "Post":
        c = [home, ("مقالات", reverse("blog:post_list"))]
        if obj.category_id:
            c.append((obj.category.title, f"{reverse('blog:post_list')}?cat={obj.category.slug}"))
        return c + [(obj.title, obj.get_absolute_url())]
    if name == "Product":
        return [home, ("محصولات", reverse("products:list")), (obj.name, obj.get_absolute_url())]
    if name == "Course":
        c = [home, ("آکادمی", reverse("academy:course_list"))]
        if getattr(obj, "category_id", None):
            c.append((obj.category.title, f"{reverse('academy:course_list')}?cat={obj.category.slug}"))
        return c + [(obj.title, obj.get_absolute_url())]
    if name == "TeamMember":
        return [home, ("تیم ما", reverse("team:list")), (obj.name, obj.get_absolute_url())]
    if name == "Book":
        c = [home, ("کتابخانه", reverse("library:list"))]
        if obj.category_id:
            c.append((obj.category.title, f"{reverse('library:list')}?cat={obj.category.slug}"))
        return c + [(obj.title, obj.get_absolute_url())]
    if name == "Game":
        return [home, ("بازی‌ها", reverse("games:list")), (obj.title, obj.get_absolute_url())]
    if name == "Page":
        return [home, (obj.title, obj.get_absolute_url())]
    return [home]


@register.simple_tag(takes_context=True)
def breadcrumbs(context, obj=None, *extra):
    """{% breadcrumbs obj %} یا {% breadcrumbs None "مقالات" "/blog/" %} — مسیر + BreadcrumbList."""
    request = context["request"]
    items = _crumbs(obj)
    if extra:
        items = [("خانه", "/")] + [(extra[i], extra[i + 1] if i + 1 < len(extra) else request.path) for i in range(0, len(extra), 2)]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": request.build_absolute_uri(u)} for i, (n, u) in enumerate(items)]}
    links = format_html_join("", '<li><a href="{}">{}</a></li>', ((u, n) for n, u in items[:-1]))
    last = escape(items[-1][0]) if items else ""
    return mark_safe(f'<nav class="crumbs" aria-label="مسیر صفحه"><ol>{links}<li aria-current="page">{last}</li></ol></nav>' + _ld(ld))
