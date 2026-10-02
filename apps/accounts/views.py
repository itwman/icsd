from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.academy.models import Attempt, Certificate, Enrollment
from .forms import MobileForm, OTPForm, PasswordLoginForm, ProfileForm, SetPasswordForm
from .models import OTP
from .sms import send_otp

User = get_user_model()


def _next(request):
    nxt = request.GET.get("next") or request.POST.get("next") or request.session.get("next")
    return nxt or reverse("accounts:dashboard")


def login_view(request):
    """صفحه‌ی ورود: موبایل → ارسال کد. تب دوم: موبایل/ایمیل + رمز."""
    if request.user.is_authenticated:
        return redirect(_next(request))
    if request.GET.get("next"):
        request.session["next"] = request.GET["next"]

    mobile_form = MobileForm(prefix="m")
    pass_form = PasswordLoginForm(prefix="p")

    if request.method == "POST":
        if "send_code" in request.POST:
            mobile_form = MobileForm(request.POST, prefix="m")
            if mobile_form.is_valid():
                mobile = mobile_form.cleaned_data["mobile"]
                otp = OTP.issue(mobile)
                send_otp(mobile, otp.code)
                request.session["otp_mobile"] = mobile
                messages.info(request, "کد ورود پیامک شد.")
                return redirect("accounts:verify")
        elif "with_password" in request.POST:
            pass_form = PasswordLoginForm(request.POST, prefix="p")
            if pass_form.is_valid():
                user = authenticate(request, username=pass_form.cleaned_data["ident"],
                                    password=pass_form.cleaned_data["password"])
                if user:
                    login(request, user)
                    return redirect(_next(request))
                pass_form.add_error(None, "اطلاعات ورود درست نیست.")

    return render(request, "accounts/login.html", {"mobile_form": mobile_form, "pass_form": pass_form})


def verify_view(request):
    mobile = request.session.get("otp_mobile")
    if not mobile:
        return redirect("accounts:login")
    form = OTPForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        if OTP.verify(mobile, form.cleaned_data["code"]):
            user, created = User.objects.get_or_create(mobile=mobile)
            if not user.mobile_verified:
                user.mobile_verified = True
                user.save(update_fields=["mobile_verified"])
            login(request, user)
            request.session.pop("otp_mobile", None)
            if created or not user.first_name:
                messages.success(request, "خوش آمدید! لطفاً نام خود را کامل کنید.")
                return redirect("accounts:profile")
            return redirect(_next(request))
        form.add_error("code", "کد نادرست یا منقضی است.")
    return render(request, "accounts/verify.html", {"form": form, "mobile": mobile})


@require_POST
def resend_view(request):
    mobile = request.session.get("otp_mobile")
    if mobile:
        otp = OTP.issue(mobile)
        send_otp(mobile, otp.code)
        messages.info(request, "کد دوباره ارسال شد.")
    return redirect("accounts:verify")


def logout_view(request):
    logout(request)
    return redirect("core:home")


@login_required
def dashboard(request):
    enrollments = (Enrollment.objects.filter(user=request.user)
                   .select_related("course", "course__category").order_by("-created_at"))
    certificates = Certificate.objects.filter(user=request.user, is_revoked=False).select_related("course")
    attempts = Attempt.objects.filter(user=request.user, finished_at__isnull=False).select_related("quiz", "quiz__course")[:12]
    return render(request, "accounts/dashboard.html", {"enrollments": enrollments, "certificates": certificates, "attempts": attempts})


@login_required
def profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    pw_form = SetPasswordForm(prefix="pw")
    if request.method == "POST":
        if "save_profile" in request.POST and form.is_valid():
            form.save()
            messages.success(request, "پروفایل ذخیره شد.")
            return redirect(request.session.pop("next", None) or "accounts:dashboard")
        if "save_password" in request.POST:
            pw_form = SetPasswordForm(request.POST, prefix="pw")
            if pw_form.is_valid():
                request.user.set_password(pw_form.cleaned_data["password1"])
                request.user.save()
                login(request, request.user)   # جلسه نپرد
                messages.success(request, "رمز عبور تنظیم شد. از این به بعد با رمز هم می‌توانید وارد شوید.")
                return redirect("accounts:profile")
    return render(request, "accounts/profile.html", {"form": form, "pw_form": pw_form})
