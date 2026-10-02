"""نقاط پایانی آژاکس: /api/ac/<entity>/"""
from django.urls import path

from apps.academy.models import Category
from apps.blog.models import Tag
from apps.leads.models import City, Province
from .views import AutocompleteView

app_name = "ac"


class TagAC(AutocompleteView):
    model = Tag


class CategoryAC(AutocompleteView):
    model = Category
    search_field = "title"
    create_field = "title"
    allow_create = False


class ProvinceAC(AutocompleteView):
    model = Province
    allow_create = False


class CityAC(AutocompleteView):
    model = City
    require_login_to_create = False   # مشتری بدون حساب هم باید بتواند شهرش را اضافه کند

    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.GET.get("province") or self.request.POST.get("province")
        if p:
            qs = qs.filter(province_id=p)
        return qs

    def post(self, request):
        import json
        try:
            data = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            data = {}
        text = (data.get("text") or "").strip()
        province_id = data.get("province")
        if not text:
            return self._json({"error": "خالی"}, 400)
        if not province_id:
            return self._json({"error": "اول استان را انتخاب کنید"}, 400)
        obj, _ = City.objects.get_or_create(name=text, province_id=province_id)
        return self._json({"value": obj.pk, "text": str(obj)})

    @staticmethod
    def _json(data, status=200):
        from django.http import JsonResponse
        return JsonResponse(data, status=status)


urlpatterns = [
    path("tag/", TagAC.as_view(), name="tag"),
    path("category/", CategoryAC.as_view(), name="category"),
    path("province/", ProvinceAC.as_view(), name="province"),
    path("city/", CityAC.as_view(), name="city"),
]
