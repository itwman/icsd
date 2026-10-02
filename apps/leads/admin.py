from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from apps.common.admin import JalaliAdminMixin
from .models import City, ProjectRequest, Province


class CityInline(TabularInline):
    model = City
    extra = 0


@admin.register(Province)
class ProvinceAdmin(ModelAdmin):
    search_fields = ("name",)
    inlines = [CityInline]


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ("name", "province")
    list_filter = ("province",)
    search_fields = ("name", "province__name")
    autocomplete_fields = ("province",)


@admin.register(ProjectRequest)
class ProjectRequestAdmin(JalaliAdminMixin, ModelAdmin):
    list_display = ("full_name", "company", "mobile", "topic", "city", "status", "assigned_to", "created_at")
    list_filter = ("status", "topic", "province", "assigned_to")
    list_editable = ("status", "assigned_to")
    search_fields = ("full_name", "company", "mobile", "email", "description")
    autocomplete_fields = ("province", "city", "product", "assigned_to")
    readonly_fields = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"
    fieldsets = (
        ("مشتری", {"fields": ("full_name", "company", "job_title", "mobile", "phone", "email")}),
        ("آدرس", {"fields": ("province", "city", "address", "postal_code")}),
        ("پروژه", {"fields": ("topic", "product", "budget", "preferred_date", "description", "attachment")}),
        ("پیگیری", {"fields": ("status", "assigned_to", "notes", "user", "created_at", "updated_at")}),
    )
