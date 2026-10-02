from django.utils.html import format_html
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin

from apps.common.admin import JalaliAdminMixin
from apps.seo.admin_mixins import SEOAdminMixin
from .models import Customer, HomeSection, NavLink, Page, SiteSettings, TimelineEvent


@admin.register(SiteSettings)
class SiteSettingsAdmin(JalaliAdminMixin, ModelAdmin):
    fieldsets = (
        ("هویت برند", {"fields": ("site_name", "short_name", "tagline", "site_url", "logo", "logo_dark", "favicon", "founded_year")}),
        ("رنگ‌ها", {"fields": ("color_primary", "color_accent")}),
        ("هیرو صفحه اصلی", {"fields": ("hero_title", "hero_highlight", "hero_subtitle", "hero_show_clock",
                                        ("hero_particles", "hero_words_logo"), "hero_words", "hero_words_interval",
                                        ("stat_1_value", "stat_1_label"), ("stat_2_value", "stat_2_label"), ("stat_3_value", "stat_3_label"))}),
        ("تماس و شبکه‌های اجتماعی", {"fields": ("phone", "mobile", "email", "address", "map_embed", "instagram", "telegram", "linkedin", "aparat")}),
        ("فوتر و سئو", {"fields": ("footer_text", "default_meta_description", "default_og_image", "head_extra_html", "enamad_html", "indexnow_key"),
                        "description": "کد تأیید گوگل سرچ‌کنسول/بینگ را در «کد اضافه‌ی head» بگذارید. کلید IndexNow: یک رشته‌ی ۳۲ حرفی دلخواه (حروف و عدد)؛ با هر انتشار، بینگ و یاندکس فوراً خبردار می‌شوند."}),
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
    list_display = ("title", "key", "is_active", "order", "items_limit")
    list_editable = ("is_active", "order", "items_limit")
    list_filter = ("key", "is_active")
    fieldsets = (
        (None, {"fields": ("key", "kicker", "title", "subtitle"),
                "description": "هر بخش را می‌توانید خاموش کنید، ترتیبش را عوض کنید یا حذف کنید. «بخش سفارشی» را هر چند بار که بخواهید اضافه کنید."}),
        ("متن آزاد (فقط بخش سفارشی)", {"classes": ("collapse",), "fields": ("body",)}),
        ("آیتم‌ها و دکمه", {"fields": ("items_limit", ("button_text", "button_url"))}),
        ("نمایش", {"fields": ("is_active", "order")}),
    )


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ("thumb", "name", "industry", "city", "show_on_home", "is_active", "order")
    list_display_links = ("thumb", "name")
    list_editable = ("show_on_home", "is_active", "order")
    list_filter = ("is_active", "show_on_home", "industry")
    search_fields = ("name", "industry", "city")
    filter_horizontal = ("products",)
    readonly_fields = ("logo_preview",)
    fieldsets = (
        (None, {"fields": ("name", "logo", "logo_preview", "website")}),
        ("اطلاعات همکاری", {"fields": (("industry", "city", "since"), "products", "description")}),
        ("نمایش", {"fields": ("show_on_home", "is_active", "order")}),
    )

    def _img(self, obj, h):
        if not obj.logo:
            return "—"
        return format_html('<img src="{}" style="height:{}px;max-width:{}px;object-fit:contain;background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:4px">',
                           obj.logo.url, h, h * 3)

    @admin.display(description="لوگو")
    def thumb(self, obj):
        return self._img(obj, 34)

    @admin.display(description="پیش‌نمایش")
    def logo_preview(self, obj):
        return self._img(obj, 90)


@admin.register(TimelineEvent)
class TimelineEventAdmin(ModelAdmin):
    list_display = ("era", "title", "is_active", "order")
    list_editable = ("is_active", "order")


@admin.register(Page)
class PageAdmin(SEOAdminMixin, ModelAdmin):
    seo_url_prefix = "/p/"
    list_display = ("title", "slug", "is_published", "show_in_footer", "updated_at", "seo_score")
    list_filter = ("is_published", "show_in_footer")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NavLink)
class NavLinkAdmin(ModelAdmin):
    list_display = ("title", "url", "is_active", "order", "new_tab")
    list_editable = ("is_active", "order")
