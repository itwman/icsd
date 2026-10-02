from django.http import Http404, HttpResponse

from apps.core.models import SiteSettings


def robots_txt(request):
    site = SiteSettings.load()
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /pay/",
        "Disallow: /api/",
        "Disallow: /ckeditor5/",
        "Disallow: /*?q=",
        "Allow: /",
        f"Sitemap: {site.site_url.rstrip('/')}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def indexnow_key(request, key):
    site = SiteSettings.load()
    if not site.indexnow_key or key != site.indexnow_key:
        raise Http404
    return HttpResponse(site.indexnow_key, content_type="text/plain")
