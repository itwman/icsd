from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin

from apps.common.admin import JalaliAdminMixin
from .models import HomeSection, NavLink, Page, SiteSettings, TimelineEvent


@admin.register(SiteSettings)
class SiteSettingsAdmin(JalaliAdminMixin, ModelAdmin):
    fieldsets = (
        ("هویت برند", {"fields": ("site_name", "short_name", "tagline", "site_url", "logo", "logo_dark", "favicon", "founded_year")}),
        ("رنگ‌ها", {"fields": ("color_primary", "color_accent")}),
        ("هیرو صفحه اصلی", {"fields": ("hero_title", "hero_highlight", "hero_subtitle", "hero_show_clock",
                                        ("hero_particles", "hero_words_logo"), "hero_words", "hero_words_interval",
                                        ("stat_1_value", "stat_1_label"), ("stat_2_value", "stat_2_label"), ("stat_3_value", "stat_3_label"))}),
        ("تماس و شبکه‌های اجتماعی", {"fields": ("phone", "mobile", "email", "address", "map_embed", "instagram", "telegram", "linkedin", "aparat")}),
        ("فوتر و سئو", {"fields": ("footer_text", "default_meta_description", "default_og_image", "head_extra_html", "enamad_html")}),
        ("درگاه پرداخت و پیامک", {"classes": ("collapse",), "fields": ("zarinpal_merchant_id", "zarinpal_sandbox", "kavenegar_api_key", "kavenegar_sender")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        return redirect(reverse("admin:core_sitesettings_change", args=[obj.pk]))


@admin.register(HomeSection)
class HomeSectionAdmin(ModelAdmin):
    list_display = ("title", "key", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("key", "is_active")


@admin.register(TimelineEvent)
class TimelineEventAdmin(ModelAdmin):
    list_display = ("era", "title", "is_active", "order")
    list_editable = ("is_active", "order")


@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ("title", "slug", "is_published", "show_in_footer", "updated_at")
    list_filter = ("is_published", "show_in_footer")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NavLink)
class NavLinkAdmin(ModelAdmin):
    list_display = ("title", "url", "is_active", "order", "new_tab")
    list_editable = ("is_active", "order")
