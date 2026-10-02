from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm
from unfold.forms import UserChangeForm as UnfoldUserChangeForm
from unfold.forms import UserCreationForm as UnfoldUserCreationForm

from apps.common.admin import JalaliAdminMixin
from .models import OTP, User


class UserCreationForm(UnfoldUserCreationForm):
    class Meta(UnfoldUserCreationForm.Meta):
        model = User
        fields = ("mobile", "first_name", "last_name")


class UserChangeForm(UnfoldUserChangeForm):
    class Meta(UnfoldUserChangeForm.Meta):
        model = User
        fields = "__all__"


admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(JalaliAdminMixin, BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    ordering = ("-date_joined",)
    list_display = ("mobile", "first_name", "last_name", "email", "is_instructor", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "is_instructor", "groups")
    search_fields = ("mobile", "first_name", "last_name", "email")
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("mobile", "password")}),
        ("اطلاعات شخصی", {"fields": ("first_name", "last_name", "father_name", "national_code", "gender", "email", "birth_date", "avatar", "bio")}),
        ("شغل و تحصیلات", {"fields": ("education", "field_of_study", "job_title", "company", "province", "city", "website", "linkedin", "show_certificates_publicly")}),
        ("نقش و دسترسی", {"fields": ("is_active", "is_instructor", "mobile_verified", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("تاریخ‌ها", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("mobile", "first_name", "last_name", "password1", "password2")}),
    )
    filter_horizontal = ("groups", "user_permissions")
    autocomplete_fields = ("province", "city")


@admin.register(OTP)
class OTPAdmin(ModelAdmin):
    list_display = ("mobile", "code", "created_at", "attempts", "is_used")
    readonly_fields = ("mobile", "code", "created_at", "attempts", "is_used")
    search_fields = ("mobile",)

    def has_add_permission(self, request):
        return False
