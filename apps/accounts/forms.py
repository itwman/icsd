from django import forms
from django.contrib.auth import get_user_model

from apps.common.forms import JalaliDateField, JalaliDateWidget, normalize_digits

User = get_user_model()


class MobileForm(forms.Form):
    mobile = forms.CharField(label="شماره موبایل", max_length=11,
                             widget=forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric",
                                                           "placeholder": "۰۹۱۲۳۴۵۶۷۸۹", "dir": "ltr", "autofocus": True}))

    def clean_mobile(self):
        m = normalize_digits(self.cleaned_data["mobile"]).strip()
        if not (len(m) == 11 and m.startswith("09") and m.isdigit()):
            raise forms.ValidationError("شماره موبایل معتبر نیست.")
        return m


class OTPForm(forms.Form):
    code = forms.CharField(label="کد پیامک‌شده", max_length=6, min_length=6,
                           widget=forms.TextInput(attrs={"class": "form-control form-control-lg text-center", "inputmode": "numeric",
                                                         "dir": "ltr", "autocomplete": "one-time-code", "autofocus": True}))

    def clean_code(self):
        return normalize_digits(self.cleaned_data["code"]).strip()


class PasswordLoginForm(forms.Form):
    ident = forms.CharField(label="موبایل یا ایمیل",
                            widget=forms.TextInput(attrs={"class": "form-control", "dir": "ltr", "autofocus": True}))
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={"class": "form-control", "dir": "ltr"}))


class ProfileForm(forms.ModelForm):
    birth_date = JalaliDateField(label="تاریخ تولد", required=False, widget=JalaliDateWidget(birth=True))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "father_name", "national_code", "gender", "birth_date", "email",
                  "education", "field_of_study", "job_title", "company", "province", "city",
                  "website", "linkedin", "bio", "avatar", "show_certificates_publicly"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "father_name": forms.TextInput(attrs={"class": "form-control"}),
            "national_code": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric", "dir": "ltr", "maxlength": 10}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "dir": "ltr"}),
            "education": forms.Select(attrs={"class": "form-select"}),
            "field_of_study": forms.TextInput(attrs={"class": "form-control"}),
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "province": forms.Select(attrs={"data-autocomplete-url": "/api/ac/province/", "data-allow-create": "false", "placeholder": "استان"}),
            "city": forms.Select(attrs={"data-autocomplete-url": "/api/ac/city/", "data-depends-on": "id_province", "placeholder": "شهر"}),
            "website": forms.URLInput(attrs={"class": "form-control", "dir": "ltr"}),
            "linkedin": forms.URLInput(attrs={"class": "form-control", "dir": "ltr"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "show_certificates_publicly": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_national_code(self):
        v = normalize_digits(self.cleaned_data.get("national_code", "")).strip()
        if v and not (len(v) == 10 and v.isdigit()):
            raise forms.ValidationError("کد ملی باید ۱۰ رقم باشد.")
        return v


class SetPasswordForm(forms.Form):
    password1 = forms.CharField(label="رمز جدید", min_length=6, widget=forms.PasswordInput(attrs={"class": "form-control", "dir": "ltr"}))
    password2 = forms.CharField(label="تکرار رمز", widget=forms.PasswordInput(attrs={"class": "form-control", "dir": "ltr"}))

    def clean(self):
        d = super().clean()
        if d.get("password1") != d.get("password2"):
            raise forms.ValidationError("دو رمز یکسان نیستند.")
        return d
