from django.core.paginator import Paginator
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, render

from .models import BlogCategory, Post, Tag


def post_list(request):
    qs = Post.objects.filter(is_published=True).select_related("category", "author")
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat")
    tag = request.GET.get("tag")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(body__icontains=q))
    if cat:
        qs = qs.filter(category__slug=cat)
    if tag:
        qs = qs.filter(tags__name=tag)
    page = Paginator(qs, 9).get_page(request.GET.get("page"))
    return render(request, "blog/post_list.html", {
        "page": page, "categories": BlogCategory.objects.all(), "q": q, "cat": cat, "tag": tag,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related("category", "author"), slug=slug, is_published=True)
    Post.objects.filter(pk=post.pk).update(views=F("views") + 1)
    related = Post.objects.filter(is_published=True, category=post.category).exclude(pk=post.pk)[:3]
    return render(request, "blog/post_detail.html", {"post": post, "related": related, "seo_obj": post})
