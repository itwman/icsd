from django.http import HttpResponse

from apps.core.models import SiteSettings


def robots_txt(request):
    site = SiteSettings.load()
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /pay/",
        "Disallow: /api/",
        "Allow: /",
        f"Sitemap: {site.site_url.rstrip('/')}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
