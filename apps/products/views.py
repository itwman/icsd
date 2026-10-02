from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, ProductTutorial


def product_list(request):
    return render(request, "products/product_list.html", {"products": Product.objects.filter(is_active=True)})


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.prefetch_related("features", "images", "related_courses"), slug=slug, is_active=True)
    tutorials = product.tutorials.all()
    if not request.user.is_authenticated:
        tutorials = tutorials.filter(is_public=True)
    return render(request, "products/product_detail.html", {"product": product, "tutorials": tutorials, "seo_obj": product})


def product_catalog(request, slug):
    """صفحه‌ی کاتالوگ چاپی — یا ریدایرکت به PDF آپلودشده."""
    product = get_object_or_404(Product.objects.prefetch_related("features", "images"), slug=slug, is_active=True)
    if product.catalog_pdf:
        return redirect(product.catalog_pdf.url)
    return render(request, "products/catalog.html", {"product": product})


def tutorial_detail(request, slug, pk):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    tutorial = get_object_or_404(ProductTutorial, pk=pk, product=product)
    if not tutorial.is_public and not request.user.is_authenticated:
        return redirect(f"/accounts/login/?next={request.path}")
    if tutorial.course_id:
        return redirect(tutorial.course)
    return render(request, "products/tutorial.html", {"product": product, "tutorial": tutorial})
