from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.common.admin import JalaliAdminMixin
from apps.seo.admin_mixins import SEOAdminMixin
from .models import BlogCategory, Post, Tag


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)


@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Post)
class PostAdmin(SEOAdminMixin, JalaliAdminMixin, ModelAdmin):
    seo_url_prefix = "/blog/"
    list_display = ("title", "category", "is_published", "published_at", "views", "seo_score")
    list_filter = ("is_published", "category", "author")
    search_fields = ("title", "excerpt", "body", "focus_keyword")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category", "tags", "author")
    readonly_fields = ("views", "updated_at")
    date_hierarchy = "published_at"
    list_per_page = 30
    fieldsets = (
        (None, {"fields": ("title", "slug", "body")}),
        ("انتشار", {"fields": (("category", "is_published"), "tags", ("published_at", "author"), ("views", "updated_at"))}),
        ("تصویر شاخص و خلاصه", {"fields": ("cover", "cover_alt", "excerpt", "read_minutes"),
                                 "description": "خلاصه و زمان مطالعه اگر خالی/صفر باشند خودکار ساخته می‌شوند."}),
    )

    def save_model(self, request, obj, form, change):
        from apps.common.html import _text, read_minutes
        if not obj.author_id:
            obj.author = request.user
        if not obj.excerpt:
            t = _text(obj.body)
            obj.excerpt = (t[:280].rsplit(" ", 1)[0] + "…") if len(t) > 280 else t
        if not obj.read_minutes or "read_minutes" not in form.changed_data:
            obj.read_minutes = read_minutes(obj.body)
        super().save_model(request, obj, form, change)
