from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from apps.common.admin import JalaliAdminMixin
from .models import Attempt, Category, Certificate, Choice, Course, Enrollment, Lesson, LessonProgress, Module, Question, Quiz


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("title", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


class ModuleInline(TabularInline):
    model = Module
    extra = 0
    fields = ("title", "order")
    ordering = ("order",)
    show_change_link = True


@admin.register(Course)
class CourseAdmin(JalaliAdminMixin, ModelAdmin):
    list_display = ("title", "category", "level", "price", "is_published", "is_featured", "order", "updated_at")
    list_filter = ("category", "level", "is_published", "is_featured")
    list_editable = ("is_published", "is_featured", "order")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category", "instructor", "tags")
    inlines = [ModuleInline]
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "instructor", "level", "tags")}),
        ("محتوا", {"fields": ("summary", "description", "cover")}),
        ("قیمت و انتشار", {"fields": ("price", "duration_minutes", "is_published", "is_featured", "order", "published_at")}),
    )


class LessonInline(StackedInline):
    model = Lesson
    extra = 0
    ordering = ("order",)
    fields = ("title", "order", "kind", "minutes", "is_preview", "video_source", "arvan_video_id", "embed_html", "video_file", "attachment", "body")
    show_change_link = True


@admin.register(Module)
class ModuleAdmin(ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ("title", "module", "kind", "minutes", "is_preview", "order")
    list_filter = ("kind", "is_preview", "module__course")
    search_fields = ("title", "module__title", "module__course__title")
    autocomplete_fields = ("module",)


class ProgressInline(TabularInline):
    model = LessonProgress
    extra = 0
    readonly_fields = ("lesson", "completed_at")
    can_delete = False


@admin.register(Enrollment)
class EnrollmentAdmin(JalaliAdminMixin, ModelAdmin):
    list_display = ("user", "course", "created_at", "is_active", "percent_display")
    list_filter = ("is_active", "course")
    search_fields = ("user__mobile", "user__first_name", "user__last_name", "course__title")
    autocomplete_fields = ("user", "course")
    inlines = [ProgressInline]

    @admin.display(description="پیشرفت")
    def percent_display(self, obj):
        return f"{obj.percent}٪"


# ─────────── آزمون و گواهینامه ───────────
class ChoiceInline(TabularInline):
    model = Choice
    extra = 0
    fields = ("text", "is_correct", "order")
    min_num = 2


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("short", "quiz", "order", "is_active")
    list_filter = ("quiz", "is_active")
    search_fields = ("text",)
    autocomplete_fields = ("quiz",)
    inlines = [ChoiceInline]

    @admin.display(description="سؤال")
    def short(self, obj):
        return obj.text[:80]


class QuestionInline(TabularInline):
    model = Question
    extra = 0
    fields = ("text", "order", "is_active")
    show_change_link = True


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("title", "course", "pass_percent", "time_limit_minutes", "question_count", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "course__title")
    autocomplete_fields = ("course",)
    inlines = [QuestionInline]

    @admin.display(description="تعداد سؤال")
    def question_count(self, obj):
        return obj.questions.count()


@admin.register(Attempt)
class AttemptAdmin(ModelAdmin):
    list_display = ("user", "quiz", "score", "passed", "started_at", "finished_at")
    list_filter = ("passed", "quiz")
    search_fields = ("user__mobile", "user__first_name", "user__last_name")
    readonly_fields = ("user", "quiz", "started_at", "finished_at", "question_ids", "answers", "score", "passed")
    date_hierarchy = "started_at"

    def has_add_permission(self, request):
        return False


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ("serial", "full_name", "course", "score", "issued_at", "is_revoked")
    list_filter = ("is_revoked", "course")
    list_editable = ("is_revoked",)
    search_fields = ("serial", "full_name", "user__mobile", "code")
    readonly_fields = ("code", "serial", "user", "course", "attempt", "score", "issued_at")
    date_hierarchy = "issued_at"

    def has_add_permission(self, request):
        return False
