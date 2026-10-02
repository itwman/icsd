"""تعریف همه‌ی بخش‌های قابل مدیریت سایت در پنل."""
from django.contrib.auth.models import Group
from django.utils.html import format_html

from apps.academy.models import (Attempt, Category, Certificate, Choice, Course, Enrollment, Lesson, Module, Question,
                                 Quiz)
from apps.accounts.models import User
from apps.analytics.models import PageView
from apps.blog.models import BlogCategory, Post, Tag
from apps.core.models import Customer, HomeSection, NavLink, Page, SiteSettings, TimelineEvent
from apps.games.models import Game, Score
from apps.leads.models import City, ProjectRequest, Province
from apps.library.models import Book, BookCategory
from apps.payments.models import Order
from apps.products.models import Product, ProductFeature, ProductImage, ProductTutorial
from apps.seo.models import NotFoundLog, Redirect, SEOMeta
from apps.team.models import Education, Experience, Publication, SocialLink, Skill, TeamMember

from .registry import Child, Inline, Resource, label, register


def _seo_score(obj, body, title):
    from apps.seo.analysis import analyze_obj
    score, _ = analyze_obj(obj, body, title)
    tone = "ok" if score >= 75 else "mid" if score >= 50 else "bad"
    return format_html('<span class="score score--{}">{}</span>', tone, score)


class SEOMixin:
    @label("سئو")
    def seo_col(self, obj):
        return _seo_score(obj, self.seo.get("body", "body"), self.seo.get("title", "title"))


# ═══════════════════ سایت و ظاهر ═══════════════════
@register
class SettingsR(Resource):
    model = SiteSettings
    key = "settings"
    title = "تنظیمات سایت"
    icon = "settings"
    group = "site"
    singleton = True
    can_add = can_delete = False
    tabs = True

    def exclude_for(self, request):
        if request.user.is_superuser:
            return ()
        return ("head_extra_html", "enamad_html", "zarinpal_merchant_id", "zarinpal_sandbox", "kavenegar_api_key", "kavenegar_sender")

    fieldsets = [
        ("هویت برند", ["site_name", "short_name", "tagline", "site_url", "founded_year", "logo", "logo_dark", "favicon"]),
        ("رنگ‌ها", ["color_primary", "color_accent"]),
        ("صفحه‌ی اصلی (هیرو)", ["hero_title", "hero_highlight", "hero_subtitle", "hero_show_clock", "hero_particles",
                                "hero_words", "hero_words_logo", "hero_words_interval",
                                "stat_1_value", "stat_1_label", "stat_2_value", "stat_2_label", "stat_3_value", "stat_3_label"]),
        ("تماس و شبکه‌ها", ["phone", "mobile", "email", "address", "map_embed", "instagram", "telegram", "linkedin", "aparat"]),
        ("فوتر و سئو", ["footer_text", "default_meta_description", "default_og_image", "indexnow_key", "enamad_html", "head_extra_html"]),
        ("درگاه و پیامک", ["zarinpal_merchant_id", "zarinpal_sandbox", "kavenegar_api_key", "kavenegar_sender"]),
    ]


@register
class HomeSectionR(Resource):
    model = HomeSection
    key = "home-sections"
    icon = "layout"
    group = "site"
    hidden_in_menu = True
    list_display = ("title", "key", "is_active", "items_limit")
    toggles = ("is_active",)
    filters = ("key", "is_active")
    can_duplicate = True
    fieldsets = [("بخش", ["key", "kicker", "title", "subtitle", "items_limit", "button_text", "button_url", "is_active", "order"]),
                 ("متن آزاد (فقط بخش سفارشی)", ["body"])]


@register
class NavLinkR(Resource):
    model = NavLink
    key = "menu-items"
    icon = "menu"
    group = "site"
    hidden_in_menu = True
    list_display = ("title", "url", "is_active", "new_tab")
    toggles = ("is_active", "new_tab")


@register
class PageR(SEOMixin, Resource):
    model = Page
    key = "pages"
    icon = "doc"
    group = "site"
    list_display = ("title", "slug", "is_published", "show_in_footer", "updated_at", "seo_col")
    toggles = ("is_published", "show_in_footer")
    search = ("title", "slug")
    filters = ("is_published",)
    seo = {"body": "body", "title": "title", "prefix": "/p/"}
    prepopulate = {"slug": "title"}
    can_duplicate = True


@register
class CustomerR(Resource):
    model = Customer
    key = "customers"
    icon = "handshake"
    group = "site"
    thumb = "logo"
    list_display = ("name", "industry", "city", "show_on_home", "is_active")
    toggles = ("show_on_home", "is_active")
    search = ("name", "industry", "city")
    filters = ("show_on_home", "is_active")


@register
class TimelineR(Resource):
    model = TimelineEvent
    key = "timeline"
    icon = "timeline"
    group = "site"
    list_display = ("era", "title", "is_active")
    toggles = ("is_active",)


# ═══════════════════ محتوا ═══════════════════
@register
class PostR(SEOMixin, Resource):
    model = Post
    key = "posts"
    title = "نوشته‌ها و مقالات"
    icon = "article"
    group = "content"
    thumb = "cover"
    list_display = ("title", "category", "is_published", "published_at", "seo_col")
    toggles = ("is_published",)
    search = ("title", "excerpt", "body")
    filters = ("is_published", "category", "author")
    select_related = ("category",)
    ordering = ("-published_at",)
    seo = {"body": "body", "title": "title", "prefix": "/blog/"}
    prepopulate = {"slug": "title"}
    can_duplicate = True
    readonly = ("views",)
    fieldsets = [("نوشته", ["title", "slug", "body"]),
                 ("انتشار", ["category", "tags", "is_published", "published_at", "author"]),
                 ("تصویر و خلاصه", ["cover", "cover_alt", "excerpt", "read_minutes"])]

    def before_save(self, request, obj, form, is_new):
        from apps.common.html import _text, read_minutes
        if not obj.author_id:
            obj.author = request.user
        if not obj.excerpt:
            t = _text(obj.body)
            obj.excerpt = (t[:280].rsplit(" ", 1)[0] + "…") if len(t) > 280 else t
        if not obj.read_minutes or "read_minutes" not in form.changed_data:
            obj.read_minutes = read_minutes(obj.body)


@register
class BlogCategoryR(Resource):
    model = BlogCategory
    key = "post-categories"
    icon = "category"
    group = "content"
    list_display = ("title", "slug", "posts_count")
    search = ("title",)
    prepopulate = {"slug": "title"}

    @label("تعداد نوشته")
    def posts_count(self, obj):
        return obj.posts.count()


@register
class TagR(Resource):
    model = Tag
    key = "tags"
    icon = "tag"
    group = "content"
    list_display = ("name",)
    search = ("name",)


@register
class ProductR(SEOMixin, Resource):
    model = Product
    key = "products"
    icon = "box"
    group = "content"
    thumb = "logo"
    list_display = ("name", "status", "version", "is_featured", "is_active", "seo_col")
    toggles = ("is_featured", "is_active")
    search = ("name", "latin_name", "tagline")
    filters = ("status", "is_active", "is_featured")
    seo = {"body": "description", "title": "name", "prefix": "/products/"}
    prepopulate = {"slug": "latin_name"}
    can_duplicate = True
    fieldsets = [("معرفی", ["name", "latin_name", "slug", "tagline", "category_label", "summary", "description", "target_audience"]),
                 ("ظاهر", ["logo", "cover", "color", "icon"]),
                 ("وضعیت و نسخه", ["status", "version", "license_label", "tech_stack", "price_note", "demo_url", "catalog_pdf"]),
                 ("نمایش", ["is_active", "is_featured", "order", "related_courses"])]
    inlines = [Inline(ProductFeature, ["title", "text", "icon", "order"], title="قابلیت‌ها"),
               Inline(ProductImage, ["image", "caption", "order"], title="گالری تصاویر"),
               Inline(ProductTutorial, ["title", "body", "embed_html", "attachment", "course", "is_public", "order"],
                      title="آموزش‌های محصول", stacked=True, extra=0)]


@register
class TeamR(SEOMixin, Resource):
    model = TeamMember
    key = "team"
    title = "تیم و رزومه‌ها"
    icon = "team"
    group = "content"
    thumb = "photo"
    list_display = ("name", "role", "degree", "is_active", "seo_col")
    toggles = ("is_active",)
    search = ("name", "name_en", "role")
    seo = {"body": "about", "title": "name", "prefix": "/team/"}
    prepopulate = {"slug": "name_en"}
    fieldsets = [("مشخصات", ["name", "name_en", "slug", "role", "role_en", "degree", "photo", "about"]),
                 ("اطلاعات تماس و کلی", ["birth_year", "show_birth_year", "city", "email", "phone", "website", "show_contact"]),
                 ("نمایش", ["is_active", "order"])]
    inlines = [Inline(Education, ["title", "org", "start", "end", "desc", "order"], extra=0),
               Inline(Experience, ["title", "org", "start", "end", "desc", "order"], extra=0),
               Inline(Skill, ["group", "name", "level", "order"], extra=0),
               Inline(Publication, ["title", "authors", "venue", "year", "url", "order"], extra=0),
               Inline(SocialLink, ["label", "url", "order"], extra=0)]


# ═══════════════════ آکادمی ═══════════════════
@register
class CourseR(SEOMixin, Resource):
    model = Course
    key = "courses"
    icon = "school"
    group = "academy"
    thumb = "cover"
    list_display = ("title", "category", "level", "lessons", "is_published", "is_featured", "seo_col")
    toggles = ("is_published", "is_featured")
    search = ("title", "summary")
    filters = ("category", "level", "is_published", "is_featured")
    select_related = ("category",)
    seo = {"body": "description", "title": "title", "prefix": "/courses/"}
    prepopulate = {"slug": "title"}
    can_duplicate = True
    fieldsets = [("دوره", ["title", "slug", "category", "level", "summary", "description", "cover"]),
                 ("جزئیات", ["instructor", "price", "duration_minutes", "tags", "published_at"]),
                 ("نمایش", ["is_published", "is_featured", "order"])]
    inlines = [Inline(Module, ["title", "order"], title="فصل‌ها", extra=1)]
    children = [Child("lessons", "درس‌ها", lambda o: {"module__course": o})]

    @label("درس")
    def lessons(self, obj):
        return obj.lesson_count


@register
class CourseCategoryR(Resource):
    model = Category
    key = "course-categories"
    icon = "category"
    group = "academy"
    list_display = ("title", "slug", "icon")
    prepopulate = {"slug": "title"}


@register
class ModuleR(Resource):
    model = Module
    key = "modules"
    icon = "list"
    group = "academy"
    hidden_in_menu = True
    list_display = ("title", "course")
    filters = ("course",)
    select_related = ("course",)
    children = [Child("lessons", "درس‌های این فصل", lambda o: {"module": o}, initial=lambda o: {"module": o.pk})]


@register
class LessonR(Resource):
    model = Lesson
    key = "lessons"
    icon = "doc"
    group = "academy"
    list_display = ("title", "module", "kind", "minutes", "is_preview")
    toggles = ("is_preview",)
    search = ("title", "body")
    filters = ("module__course", "kind", "is_preview")
    select_related = ("module", "module__course")
    ordering = ("module__course__order", "module__order", "order", "id")
    prepopulate = {"slug": "title"}
    fieldsets = [("درس", ["module", "title", "slug", "kind", "minutes", "is_preview", "order", "body"]),
                 ("ویدیو و پیوست", ["video_source", "arvan_video_id", "embed_html", "video_file", "attachment"])]


@register
class QuizR(Resource):
    model = Quiz
    key = "quizzes"
    icon = "quiz"
    group = "academy"
    list_display = ("title", "course", "pass_percent", "questions_n", "is_active")
    toggles = ("is_active",)
    search = ("title",)
    select_related = ("course",)
    children = [Child("questions", "سؤال‌ها", lambda o: {"quiz": o}, initial=lambda o: {"quiz": o.pk})]

    @label("سؤال")
    def questions_n(self, obj):
        return obj.questions.count()


@register
class QuestionR(Resource):
    model = Question
    key = "questions"
    icon = "quiz"
    group = "academy"
    hidden_in_menu = True
    list_display = ("short", "quiz", "is_active")
    toggles = ("is_active",)
    search = ("text",)
    filters = ("quiz",)
    inlines = [Inline(Choice, ["text", "is_correct", "order"], title="گزینه‌ها", extra=4, max_num=8)]

    @label("سؤال")
    def short(self, obj):
        return obj.text[:90]


@register
class EnrollmentR(Resource):
    model = Enrollment
    key = "enrollments"
    title = "ثبت‌نام‌ها"
    icon = "users"
    group = "academy"
    list_display = ("user", "course", "created_at", "progress", "is_active")
    toggles = ("is_active",)
    search = ("user__mobile", "user__first_name", "user__last_name", "course__title")
    filters = ("course", "is_active")
    select_related = ("user", "course")
    can_add = False

    @label("پیشرفت")
    def progress(self, obj):
        return format_html('<span class="bar"><i style="width:{}%"></i></span> {}٪', obj.percent, obj.percent)


@register
class AttemptR(Resource):
    model = Attempt
    key = "attempts"
    icon = "history"
    group = "academy"
    list_display = ("user", "quiz", "score", "passed", "started_at")
    filters = ("quiz", "passed")
    search = ("user__mobile",)
    select_related = ("user", "quiz")
    view_perm_only = True


@register
class CertificateR(Resource):
    model = Certificate
    key = "certificates"
    icon = "award"
    group = "academy"
    list_display = ("serial", "full_name", "course", "score", "issued_at", "is_revoked")
    toggles = ("is_revoked",)
    search = ("serial", "full_name", "user__mobile")
    filters = ("course", "is_revoked")
    select_related = ("course",)
    can_add = False
    readonly = ("user", "course", "attempt", "score")


# ═══════════════════ کسب‌وکار ═══════════════════
@register
class LeadR(Resource):
    model = ProjectRequest
    key = "leads"
    title = "درخواست‌های پروژه"
    icon = "inbox"
    group = "business"
    list_display = ("full_name", "company", "mobile", "topic", "status", "created_at")
    quick_choices = ("status",)
    search = ("full_name", "company", "mobile", "email", "description")
    filters = ("status", "topic", "assigned_to")
    select_related = ("city", "province")
    badge = staticmethod(lambda: ProjectRequest.objects.filter(status="new").count())
    fieldsets = [("پیگیری", ["status", "assigned_to", "notes"]),
                 ("مشتری", ["full_name", "company", "job_title", "mobile", "phone", "email"]),
                 ("آدرس", ["province", "city", "address", "postal_code"]),
                 ("پروژه", ["topic", "product", "budget", "preferred_date", "description", "attachment"])]


@register
class OrderR(Resource):
    model = Order
    key = "orders"
    icon = "cart"
    group = "business"
    list_display = ("pk", "user", "course", "amount", "status", "created_at", "paid_at")
    filters = ("status", "course")
    search = ("user__mobile", "ref_id", "authority")
    select_related = ("user", "course")
    can_add = False
    readonly = ("user", "course", "amount", "gateway", "authority", "ref_id", "card_pan", "paid_at")


@register
class ProvinceR(Resource):
    model = Province
    key = "provinces"
    title = "استان‌ها و شهرها"
    icon = "map"
    group = "business"
    list_display = ("name", "cities_n")
    search = ("name",)
    inlines = [Inline(City, ["name"], title="شهرها", extra=1)]

    @label("شهر")
    def cities_n(self, obj):
        return obj.cities.count()


# ═══════════════════ کتابخانه و بازی ═══════════════════
@register
class BookR(SEOMixin, Resource):
    model = Book
    key = "books"
    title = "کتاب‌ها"
    icon = "book"
    group = "fun"
    thumb = "cover"
    list_display = ("title", "authors", "category", "download_count", "is_featured", "is_published", "seo_col")
    toggles = ("is_published", "is_featured")
    search = ("title", "authors", "excerpt")
    filters = ("category", "kind", "is_published")
    select_related = ("category",)
    seo = {"body": "description", "title": "title", "prefix": "/library/"}
    prepopulate = {"slug": "title"}
    can_duplicate = True
    fieldsets = [("کتاب", ["title", "slug", "subtitle", "category", "kind", "excerpt", "description"]),
                 ("شناسنامه", ["authors", "translator", "publisher", "year", "edition", "pages", "language", "isbn"]),
                 ("جلد و فایل", ["cover", "cover_alt", "file", "download_url", "preview_url", "file_format", "file_size", "require_login"]),
                 ("انتشار", ["is_published", "is_featured", "published_at", "order", "download_count"])]


@register
class BookCategoryR(Resource):
    model = BookCategory
    key = "book-categories"
    icon = "category"
    group = "fun"
    list_display = ("title", "slug")
    prepopulate = {"slug": "title"}


@register
class GameR(SEOMixin, Resource):
    model = Game
    key = "games"
    icon = "game"
    group = "fun"
    list_display = ("title", "engine", "difficulty", "play_count", "is_active", "seo_col")
    toggles = ("is_active",)
    seo = {"body": "description", "title": "title", "prefix": "/games/"}
    fieldsets = [("بازی", ["title", "slug", "engine", "emoji", "color", "difficulty", "summary", "how_to", "description", "cover"]),
                 ("تنظیمات", ["words", "leaderboard_size", "is_active", "order", "play_count"])]
    children = [Child("scores", "امتیازهای ثبت‌شده", lambda o: {"game": o})]


@register
class ScoreR(Resource):
    model = Score
    key = "scores"
    title = "جدول امتیازات"
    icon = "star"
    group = "fun"
    list_display = ("player_name", "game", "score", "created_at", "is_hidden")
    toggles = ("is_hidden",)
    search = ("player_name",)
    filters = ("game", "is_hidden")
    select_related = ("game",)
    ordering = ("-score",)
    can_add = False


# ═══════════════════ سئو ═══════════════════
@register
class RedirectR(Resource):
    model = Redirect
    key = "redirects"
    icon = "redirect"
    group = "seo"
    list_display = ("old_path", "new_path", "status_code", "hits", "is_active")
    toggles = ("is_active",)
    search = ("old_path", "new_path")
    filters = ("status_code", "is_active")


@register
class NotFoundR(Resource):
    model = NotFoundLog
    key = "404"
    title = "نمایشگر ۴۰۴"
    icon = "alert"
    group = "seo"
    list_display = ("path", "hits", "last_seen", "referrer", "redirect_to", "resolved")
    toggles = ("resolved",)
    search = ("path", "referrer")
    filters = ("resolved",)
    ordering = ("resolved", "-hits")
    can_add = False
    readonly = ("hits", "referrer")
    badge = staticmethod(lambda: NotFoundLog.objects.filter(resolved=False, hits__gte=3).count())

    def before_save(self, request, obj, form, is_new):
        if obj.redirect_to:
            Redirect.objects.update_or_create(old_path=obj.path, defaults={"new_path": obj.redirect_to, "status_code": 301, "is_active": True})
            obj.resolved = True


@register
class SEOMetaR(Resource):
    model = SEOMeta
    key = "seo-meta"
    title = "متای صفحات دلخواه"
    icon = "target"
    group = "seo"
    list_display = ("path", "title", "noindex")
    toggles = ("noindex",)
    search = ("path", "title")


@register
class PageViewR(Resource):
    model = PageView
    key = "pageviews"
    title = "بازدیدها (خام)"
    icon = "chart"
    group = "seo"
    hidden_in_menu = True
    list_display = ("path", "device", "referrer", "created_at")
    filters = ("device",)
    search = ("path", "referrer")
    view_perm_only = True
    per_page = 50


# ═══════════════════ کاربران ═══════════════════
@register
class UserR(Resource):
    model = User
    key = "accounts-user"
    title = "کاربران"
    icon = "users"
    group = "people"
    thumb = "avatar"
    list_display = ("mobile", "full_name", "is_staff", "is_active", "is_instructor", "date_joined")
    toggles = ("is_active",)
    search = ("mobile", "first_name", "last_name", "email", "company")
    filters = ("is_staff", "is_active", "is_instructor", "groups")
    ordering = ("-date_joined",)
    exclude = ("password", "user_permissions", "last_login", "date_joined")
    fieldsets = [("حساب", ["mobile", "first_name", "last_name", "email", "is_active", "mobile_verified"]),
                 ("دسترسی پنل", ["is_staff", "is_superuser", "groups"]),
                 ("آکادمی", ["is_instructor", "job_title", "bio", "avatar"]),
                 ("پروفایل", ["father_name", "national_code", "gender", "birth_date", "education", "field_of_study",
                              "company", "province", "city", "website", "linkedin", "show_certificates_publicly"])]

    def exclude_for(self, request):
        return () if request.user.is_superuser else ("is_superuser", "is_staff", "groups")

    @label("نام")
    def full_name(self, obj):
        return obj.get_full_name() or "—"

    def before_save(self, request, obj, form, is_new):
        pw = (request.POST.get("new_password") or "").strip()
        if pw:
            obj.set_password(pw)
        elif is_new:
            obj.set_unusable_password()
        if not request.user.is_superuser:
            # فقط مدیر ارشد می‌تواند مدیر ارشد بسازد یا بگیرد
            old = User.objects.filter(pk=obj.pk).values_list("is_superuser", flat=True).first() if obj.pk else False
            obj.is_superuser = bool(old)


GROUP_MODEL = Group
