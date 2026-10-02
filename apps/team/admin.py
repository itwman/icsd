from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline

from apps.seo.admin_mixins import SEOAdminMixin
from .models import Education, Experience, Publication, SocialLink, Skill, TeamMember


class EducationInline(TabularInline):
    model = Education
    extra = 0
    fields = ("title", "org", "start", "end", "desc", "order")


class ExperienceInline(TabularInline):
    model = Experience
    extra = 0
    fields = ("title", "org", "start", "end", "desc", "order")


class PublicationInline(TabularInline):
    model = Publication
    extra = 0
    fields = ("title", "url", "authors", "venue", "year", "order")


class SkillInline(TabularInline):
    model = Skill
    extra = 0
    fields = ("group", "name", "level", "order")


class SocialInline(TabularInline):
    model = SocialLink
    extra = 0
    fields = ("label", "url", "order")


@admin.register(TeamMember)
class TeamMemberAdmin(SEOAdminMixin, ModelAdmin):
    seo_body_field = "about"
    seo_title_field = "name"
    seo_url_prefix = "/team/"
    list_display = ("thumb", "name", "role", "degree", "is_active", "order", "seo_score")
    list_display_links = ("thumb", "name")
    list_editable = ("is_active", "order")
    search_fields = ("name", "name_en", "role")
    prepopulated_fields = {"slug": ("name_en",)}
    inlines = [EducationInline, ExperienceInline, PublicationInline, SkillInline, SocialInline]
    fieldsets = (
        (None, {"fields": ("name", "name_en", "slug", ("role", "role_en"), "degree", "photo", "about")}),
        ("اطلاعات تماس و شخصی", {"fields": (("email", "phone", "website"), ("city", "birth_year"), ("show_contact", "show_birth_year"))}),
        ("نمایش", {"fields": ("is_active", "order")}),
    )

    @admin.display(description="تصویر")
    def thumb(self, obj):
        if not obj.photo:
            return "—"
        return format_html('<img src="{}" style="width:38px;height:38px;border-radius:50%;object-fit:cover">', obj.photo.url)
