from .models import NavLink, Page, SiteSettings


def site(request):
    return {
        "site": SiteSettings.load(),
        "nav_links": NavLink.objects.filter(is_active=True),
        "footer_pages": Page.objects.filter(is_published=True, show_in_footer=True),
    }
