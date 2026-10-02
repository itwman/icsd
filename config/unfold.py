"""پیکربندی پنل مدیریت (django-unfold) — فارسی، راست‌چین، با منوی کناری."""
from django.urls import reverse_lazy
from django.templatetags.static import static


def _perm(codename):
    return lambda request: request.user.has_perm(codename)


UNFOLD = {
    "SITE_TITLE": "پنل مدیریت",
    "SITE_HEADER": "توسعه هوشمند فرش ایرانیان",
    "SITE_SYMBOL": "hub",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "STYLES": [lambda request: static("vendor/jalali-datepicker/jalalidatepicker.min.css"),
               lambda request: static("css/admin.css")],
    "SCRIPTS": [lambda request: static("vendor/jalali-datepicker/jalalidatepicker.min.js"),
                lambda request: static("js/admin.js")],
    "DASHBOARD_CALLBACK": "apps.analytics.dashboard.callback",
    "COLORS": {
        "primary": {
            "50": "236 250 245", "100": "212 244 232", "200": "173 234 212",
            "300": "125 218 188", "400": "75 195 160", "500": "30 158 123",
            "600": "24 132 103", "700": "20 106 83", "800": "18 84 67",
            "900": "15 69 56", "950": "6 40 32",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "نمای کلی",
                "items": [
                    {"title": "داشبورد", "icon": "dashboard", "link": reverse_lazy("admin:index")},
                    {"title": "آمار بازدید", "icon": "monitoring",
                     "link": reverse_lazy("admin:analytics_pageview_changelist")},
                ],
            },
            {
                "title": "محتوای سایت",
                "separator": True,
                "items": [
                    {"title": "تنظیمات سایت", "icon": "settings",
                     "link": reverse_lazy("admin:core_sitesettings_changelist")},
                    {"title": "بخش‌های صفحه اصلی", "icon": "view_quilt",
                     "link": reverse_lazy("admin:core_homesection_changelist")},
                    {"title": "خط زمان کاشان", "icon": "timeline",
                     "link": reverse_lazy("admin:core_timelineevent_changelist")},
                    {"title": "صفحات", "icon": "description",
                     "link": reverse_lazy("admin:core_page_changelist")},
                    {"title": "منو", "icon": "menu",
                     "link": reverse_lazy("admin:core_navlink_changelist")},
                ],
            },
            {
                "title": "آکادمی",
                "separator": True,
                "items": [
                    {"title": "دوره‌ها", "icon": "school", "link": reverse_lazy("admin:academy_course_changelist")},
                    {"title": "دسته‌بندی‌ها", "icon": "category", "link": reverse_lazy("admin:academy_category_changelist")},
                    {"title": "ثبت‌نام‌ها", "icon": "how_to_reg", "link": reverse_lazy("admin:academy_enrollment_changelist")},
                    {"title": "آزمون‌ها", "icon": "quiz", "link": reverse_lazy("admin:academy_quiz_changelist")},
                    {"title": "سؤال‌ها", "icon": "help", "link": reverse_lazy("admin:academy_question_changelist")},
                    {"title": "نوبت‌های آزمون", "icon": "fact_check", "link": reverse_lazy("admin:academy_attempt_changelist")},
                    {"title": "گواهینامه‌ها", "icon": "workspace_premium", "link": reverse_lazy("admin:academy_certificate_changelist")},
                ],
            },
            {
                "title": "محصولات و وبلاگ",
                "separator": True,
                "items": [
                    {"title": "محصولات", "icon": "inventory_2", "link": reverse_lazy("admin:products_product_changelist")},
                    {"title": "نوشته‌ها", "icon": "article", "link": reverse_lazy("admin:blog_post_changelist")},
                    {"title": "برچسب‌ها", "icon": "sell", "link": reverse_lazy("admin:blog_tag_changelist")},
                ],
            },
            {
                "title": "مشتریان و فروش",
                "separator": True,
                "items": [
                    {"title": "درخواست‌های پروژه", "icon": "request_quote", "link": reverse_lazy("admin:leads_projectrequest_changelist")},
                    {"title": "سفارش‌ها", "icon": "receipt_long", "link": reverse_lazy("admin:payments_order_changelist")},
                ],
            },
            {
                "title": "کاربران و دسترسی",
                "separator": True,
                "items": [
                    {"title": "کاربران", "icon": "person", "link": reverse_lazy("admin:accounts_user_changelist")},
                    {"title": "نقش‌ها (گروه‌ها)", "icon": "admin_panel_settings", "link": reverse_lazy("admin:auth_group_changelist")},
                ],
            },
            {
                "title": "سئو",
                "separator": True,
                "items": [
                    {"title": "متادیتای صفحات", "icon": "travel_explore", "link": reverse_lazy("admin:seo_seometa_changelist")},
                    {"title": "ریدایرکت‌ها", "icon": "alt_route", "link": reverse_lazy("admin:seo_redirect_changelist")},
                ],
            },
        ],
    },
}
