from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.common.admin import JalaliAdminMixin
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
class PostAdmin(JalaliAdminMixin, ModelAdmin):
    list_display = ("title", "category", "author", "is_published", "published_at", "views")
    list_filter = ("is_published", "category", "author")
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category", "tags", "author")
    readonly_fields = ("views", "updated_at")
    date_hierarchy = "published_at"

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
