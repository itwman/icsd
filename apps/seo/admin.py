from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Redirect, SEOMeta


@admin.register(SEOMeta)
class SEOMetaAdmin(ModelAdmin):
    list_display = ("path", "title", "noindex")
    search_fields = ("path", "title", "description")
    list_filter = ("noindex",)


@admin.register(Redirect)
class RedirectAdmin(ModelAdmin):
    list_display = ("old_path", "new_path", "status_code", "hits", "is_active")
    list_editable = ("is_active",)
    search_fields = ("old_path", "new_path")
    list_filter = ("status_code", "is_active")
