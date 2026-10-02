from django.contrib import admin, messages
from unfold.admin import ModelAdmin

from .models import NotFoundLog, Redirect, SEOMeta


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


@admin.register(NotFoundLog)
class NotFoundLogAdmin(ModelAdmin):
    list_display = ("path", "hits", "last_seen", "referrer", "redirect_to", "resolved")
    list_editable = ("redirect_to",)
    list_filter = ("resolved",)
    search_fields = ("path", "referrer")
    readonly_fields = ("path", "hits", "referrer", "first_seen", "last_seen")
    actions = ("mark_gone", "mark_resolved")

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        if obj.redirect_to:
            Redirect.objects.update_or_create(old_path=obj.path, defaults={"new_path": obj.redirect_to, "status_code": 301, "is_active": True})
            obj.resolved = True
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

    @admin.action(description="ساخت ریدایرکت برای ردیف‌هایی که «ریدایرکت به» دارند")
    def mark_resolved(self, request, queryset):
        n = 0
        for o in queryset.exclude(redirect_to=""):
            Redirect.objects.update_or_create(old_path=o.path, defaults={"new_path": o.redirect_to, "status_code": 301, "is_active": True})
            o.resolved = True
            o.save(update_fields=["resolved"])
            n += 1
        messages.success(request, f"{n} ریدایرکت ساخته شد.")

    @admin.action(description="علامت «حذف شده» (۴۱۰) — به گوگل بگو این صفحه دیگر نیست")
    def mark_gone(self, request, queryset):
        for o in queryset:
            Redirect.objects.update_or_create(old_path=o.path, defaults={"new_path": "", "status_code": 410, "is_active": True})
        queryset.update(resolved=True)
        messages.success(request, "ثبت شد.")
