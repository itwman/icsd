"""SEOAdminMixin: بخش «سئو» + پنل زنده‌ی امتیاز و پیش‌نمایش گوگل در فرم ادمین + ستون امتیاز در فهرست."""
from django.contrib import admin
from django.utils.html import format_html

from .analysis import analyze_obj

SEO_TITLE = "سئو و موتورهای جستجو"
SEO_FIELDS = ("focus_keyword", "seo_title", "meta_description", "canonical_url", "noindex")


class SEOAdminMixin:
    seo_body_field = "body"
    seo_title_field = "title"
    seo_url_prefix = "/"

    class Media:
        css = {"all": ("css/seo-panel.css",)}
        js = ("js/seo-panel.js",)

    def get_fieldsets(self, request, obj=None):
        from django.utils.html import escape
        from apps.core.models import SiteSettings
        site = SiteSettings.load()
        fs = [f for f in super().get_fieldsets(request, obj) if f[0] != SEO_TITLE]
        # فیلدهای سئو را از بقیه‌ی fieldsetها حذف کن (اگر Django خودش اضافه کرده باشد)
        clean = []
        for name, opts in fs:
            fields = [f for f in opts.get("fields", ()) if f not in SEO_FIELDS]
            clean.append((name, {**opts, "fields": fields}))
        panel = (f'<div id="seo-panel" class="seo-panel" data-site="{escape(site.site_name)}" '
                 f'data-url="{escape(site.site_url.rstrip("/"))}" data-body="{self.seo_body_field}" '
                 f'data-title="{self.seo_title_field}" data-prefix="{escape(self.seo_url_prefix)}"></div>')
        clean.insert(1, (SEO_TITLE, {"fields": SEO_FIELDS, "description": panel}))
        return clean

    @admin.display(description="سئو")
    def seo_score(self, obj):
        score, _ = analyze_obj(obj, self.seo_body_field, self.seo_title_field)
        color = "#16a34a" if score >= 75 else "#d97706" if score >= 50 else "#dc2626"
        return format_html('<b style="color:{};font-variant-numeric:tabular-nums">{}</b>', color, score)
