from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ("id", "user", "course", "amount", "status", "ref_id", "created_at", "paid_at")
    list_filter = ("status", "gateway", "course")
    search_fields = ("user__mobile", "user__first_name", "user__last_name", "authority", "ref_id")
    readonly_fields = ("authority", "ref_id", "card_pan", "created_at", "paid_at")
    autocomplete_fields = ("user", "course")
    date_hierarchy = "created_at"
