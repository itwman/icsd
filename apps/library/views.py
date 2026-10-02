from django.contrib.auth.views import redirect_to_login
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, BookCategory


def book_list(request):
    qs = Book.objects.filter(is_published=True).select_related("category")
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat", "")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(authors__icontains=q) | Q(excerpt__icontains=q) | Q(subtitle__icontains=q))
    if cat:
        qs = qs.filter(category__slug=cat)
    page = Paginator(qs, 12).get_page(request.GET.get("page"))
    cats = BookCategory.objects.filter(books__is_published=True).distinct()
    return render(request, "library/book_list.html", {"page": page, "q": q, "cat": cat, "categories": cats})


def book_detail(request, slug):
    book = get_object_or_404(Book.objects.select_related("category"), slug=slug, is_published=True)
    Book.objects.filter(pk=book.pk).update(view_count=F("view_count") + 1)
    related = Book.objects.filter(is_published=True).exclude(pk=book.pk)
    if book.category_id:
        related = related.filter(category_id=book.category_id)
    return render(request, "library/book_detail.html", {"book": book, "seo_obj": book, "related": related[:4]})


def book_download(request, slug):
    book = get_object_or_404(Book, slug=slug, is_published=True)
    if not book.has_download:
        raise Http404
    if book.require_login and not request.user.is_authenticated:
        return redirect_to_login(book.get_absolute_url())
    Book.objects.filter(pk=book.pk).update(download_count=F("download_count") + 1)
    return redirect(book.file.url if book.file else book.download_url)
