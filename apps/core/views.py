from django.shortcuts import get_object_or_404, render

from apps.academy.models import Course
from apps.blog.models import Post
from apps.products.models import Product
from .models import Customer, HomeSection, Page, TimelineEvent


def home(request):
    """هر بخش فعال، آیتم‌های خودش را (با سقف «حداکثر تعداد آیتم») در s.items می‌گیرد."""
    sections = list(HomeSection.objects.filter(is_active=True))
    for s in sections:
        if s.key == "products":
            qs = Product.objects.filter(is_active=True)
            featured = qs.filter(is_featured=True)
            s.items = s.limit(featured if featured.exists() else qs)
        elif s.key == "customers":
            s.items = s.limit(Customer.objects.filter(is_active=True, show_on_home=True))
        elif s.key == "academy":
            s.items = s.limit(Course.objects.filter(is_published=True).select_related("category"))
        elif s.key == "blog":
            s.items = s.limit(Post.objects.filter(is_published=True).select_related("category"))
        elif s.key == "team":
            from apps.team.models import TeamMember
            s.items = s.limit(TeamMember.objects.filter(is_active=True))
        elif s.key == "library":
            from apps.library.models import Book
            qs = Book.objects.filter(is_published=True).select_related("category")
            featured = qs.filter(is_featured=True)
            s.items = s.limit(featured if featured.exists() else qs)
        elif s.key == "games":
            from apps.games.models import Game
            s.items = s.limit(Game.objects.filter(is_active=True))
        elif s.key == "timeline":
            s.items = TimelineEvent.objects.filter(is_active=True)
        else:
            s.items = []
    return render(request, "core/home.html", {"sections": sections})


def customers(request):
    items = Customer.objects.filter(is_active=True).prefetch_related("products")
    return render(request, "core/customers.html", {"customers": items})


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "core/page.html", {"page": page, "seo_obj": page})


def page_not_found(request, exception=None):
    return render(request, "404.html", status=404)


def server_error(request):
    return render(request, "500.html", status=500)
