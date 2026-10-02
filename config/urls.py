from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.seo.sitemaps import SITEMAPS
from apps.academy.views import verify
from apps.seo.views import robots_txt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("", include("apps.core.urls", namespace="core")),
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("courses/", include("apps.academy.urls", namespace="academy")),
    path("products/", include("apps.products.urls", namespace="products")),
    path("blog/", include("apps.blog.urls", namespace="blog")),
    path("start-project/", include("apps.leads.urls", namespace="leads")),
    path("pay/", include("apps.payments.urls", namespace="payments")),
    path("api/ac/", include("apps.common.urls", namespace="ac")),
    path("verify/<uuid:code>/", verify, name="verify"),
    path("sitemap.xml", sitemap, {"sitemaps": SITEMAPS}, name="sitemap"),
    path("robots.txt", robots_txt, name="robots"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "apps.core.views.page_not_found"
handler500 = "apps.core.views.server_error"
