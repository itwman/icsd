from django import forms

from apps.common.forms import JalaliDateField, JalaliDateWidget, normalize_digits
from .models import City, ProjectRequest, Province


class ProjectRequestForm(forms.ModelForm):
    preferred_date = JalaliDateField(label="تاریخ مناسب برای جلسه", required=False,
                                     widget=JalaliDateWidget(attrs={"data-jdp-min-date": "today"}))

    class Meta:
        model = ProjectRequest
        fields = ["full_name", "company", "job_title", "mobile", "phone", "email",
                  "province", "city", "address", "postal_code",
                  "topic", "product", "budget", "preferred_date", "description", "attachment"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "autocomplete": "name"}),
            "company": forms.TextInput(attrs={"class": "form-control", "autocomplete": "organization"}),
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric", "dir": "ltr", "placeholder": "۰۹۱۲۳۴۵۶۷۸۹"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric", "dir": "ltr"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "dir": "ltr"}),
            "province": forms.Select(attrs={"data-autocomplete-url": "/api/ac/province/", "data-allow-create": "false", "placeholder": "استان را جستجو کنید"}),
            "city": forms.Select(attrs={"data-autocomplete-url": "/api/ac/city/", "data-depends-on": "id_province", "placeholder": "شهر — نبود؟ تایپ کنید تا اضافه شود"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "postal_code": forms.TextInput(attrs={"class": "form-control", "inputmode": "numeric", "dir": "ltr", "maxlength": 10}),
            "topic": forms.Select(attrs={"class": "form-select"}),
            "product": forms.Select(attrs={"class": "form-select"}),
            "budget": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "مسئله را همان‌طور که در کارخانه یا شرکت می‌بینید بنویسید."}),
            "attachment": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # گزینه‌ها با آژاکس لود می‌شوند؛ فقط مقدار انتخاب‌شده را نگه می‌داریم
        self.fields["province"].queryset = Province.objects.all()
        self.fields["city"].queryset = City.objects.all()
        self.fields["province"].required = True
        self.fields["city"].required = True

    def clean_mobile(self):
        m = normalize_digits(self.cleaned_data["mobile"]).strip()
        if not (len(m) == 11 and m.startswith("09") and m.isdigit()):
            raise forms.ValidationError("شماره موبایل معتبر نیست.")
        return m

    def clean_postal_code(self):
        return normalize_digits(self.cleaned_data.get("postal_code", "")).strip()

    def clean_phone(self):
        return normalize_digits(self.cleaned_data.get("phone", "")).strip()
