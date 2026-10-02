from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import PageView


@admin.register(PageView)
class PageViewAdmin(ModelAdmin):
    list_display = ("path", "device", "user", "referrer_short", "created_at")
    list_filter = ("device", "created_at")
    search_fields = ("path", "referrer", "user__mobile")
    readonly_fields = [f.name for f in PageView._meta.fields]
    date_hierarchy = "created_at"
    list_per_page = 50

    @admin.display(description="ارجاع")
    def referrer_short(self, obj):
        return (obj.referrer or "")[:50]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
