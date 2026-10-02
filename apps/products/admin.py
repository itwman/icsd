from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from .models import Product, ProductFeature, ProductImage, ProductTutorial


class FeatureInline(TabularInline):
    model = ProductFeature
    extra = 0
    fields = ("title", "text", "icon", "order")


class ImageInline(TabularInline):
    model = ProductImage
    extra = 0
    fields = ("image", "caption", "order")


class TutorialInline(StackedInline):
    model = ProductTutorial
    extra = 0
    fields = ("title", "order", "is_public", "course", "embed_html", "attachment", "body")
    autocomplete_fields = ("course",)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("name", "latin_name", "category_label", "is_active", "is_featured", "order")
    list_editable = ("is_active", "is_featured", "order")
    list_filter = ("is_active", "is_featured")
    search_fields = ("name", "latin_name", "tagline")
    prepopulated_fields = {"slug": ("latin_name",)}
    autocomplete_fields = ("related_courses",)
    inlines = [FeatureInline, ImageInline, TutorialInline]
    fieldsets = (
        (None, {"fields": ("name", "latin_name", "slug", "tagline", "category_label", "color", "icon", "cover", "logo")}),
        ("محتوا", {"fields": ("summary", "description", "target_audience", "tech_stack")}),
        ("کاتالوگ و لینک‌ها", {"fields": ("catalog_pdf", "demo_url", "price_note", "related_courses")}),
        ("نمایش", {"fields": ("is_active", "is_featured", "order")}),
    )


@admin.register(ProductTutorial)
class ProductTutorialAdmin(ModelAdmin):
    list_display = ("title", "product", "is_public", "order")
    list_filter = ("product", "is_public")
    search_fields = ("title",)
    autocomplete_fields = ("product", "course")
