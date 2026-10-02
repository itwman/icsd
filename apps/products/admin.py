from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from apps.seo.admin_mixins import SEOAdminMixin

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


def logo_thumb(obj, size=40):
    if not getattr(obj, "logo", None):
        return "—"
    return format_html('<img src="{}" style="width:{}px;height:{}px;object-fit:contain;background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:3px">',
                       obj.logo.url, size, size)


@admin.register(Product)
class ProductAdmin(SEOAdminMixin, ModelAdmin):
    seo_body_field = "description"
    seo_title_field = "name"
    seo_url_prefix = "/products/"
    list_display = ("thumb", "name", "latin_name", "status", "version", "is_active", "is_featured", "order", "seo_score")
    list_display_links = ("thumb", "name")
    list_editable = ("is_active", "is_featured", "order")
    list_filter = ("is_active", "is_featured", "status")
    search_fields = ("name", "latin_name", "tagline")
    prepopulated_fields = {"slug": ("latin_name",)}
    autocomplete_fields = ("related_courses",)
    readonly_fields = ("logo_preview",)
    inlines = [FeatureInline, ImageInline, TutorialInline]
    fieldsets = (
        (None, {"fields": ("name", "latin_name", "slug", "tagline", "category_label")}),
        ("لوگو و ظاهر", {"fields": ("logo", "logo_preview", "color", "icon", "cover"),
                          "description": "لوگو: مربع ۵۱۲×۵۱۲ پیکسل، PNG شفاف یا SVG. روی کارت‌ها داخل کادر روشن نمایش داده می‌شود."}),
        ("وضعیت و نسخه", {"fields": (("status", "version", "license_label"),)}),
        ("محتوا", {"fields": ("summary", "description", "target_audience", "tech_stack")}),
        ("کاتالوگ و لینک‌ها", {"fields": ("catalog_pdf", "demo_url", "price_note", "related_courses")}),
        ("نمایش", {"fields": ("is_active", "is_featured", "order")}),
    )

    @admin.display(description="لوگو")
    def thumb(self, obj):
        return logo_thumb(obj)

    @admin.display(description="پیش‌نمایش لوگو")
    def logo_preview(self, obj):
        return logo_thumb(obj, 120)


@admin.register(ProductTutorial)
class ProductTutorialAdmin(ModelAdmin):
    list_display = ("title", "product", "is_public", "order")
    list_filter = ("product", "is_public")
    search_fields = ("title",)
    autocomplete_fields = ("product", "course")
