from django.shortcuts import get_object_or_404, render

from apps.academy.models import Course
from apps.blog.models import Post
from apps.products.models import Product
from .models import HomeSection, Page, TimelineEvent


def home(request):
    sections = HomeSection.objects.filter(is_active=True)
    return render(request, "core/home.html", {
        "sections": sections,
        "products": Product.objects.filter(is_active=True)[:8],
        "courses": Course.objects.filter(is_published=True).select_related("category")[:6],
        "posts": Post.objects.filter(is_published=True).select_related("category")[:3],
        "timeline": TimelineEvent.objects.filter(is_active=True),
    })


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "core/page.html", {"page": page, "seo_obj": page})


def page_not_found(request, exception=None):
    return render(request, "404.html", status=404)


def server_error(request):
    return render(request, "500.html", status=500)
