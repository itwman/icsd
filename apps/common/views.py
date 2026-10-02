"""ویوی عمومی جستجوی آژاکسی با ایجاد خودکار (Tom Select)."""
import json

from django.http import HttpResponseForbidden, JsonResponse
from django.views import View


class AutocompleteView(View):
    model = None
    search_field = "name"
    create_field = "name"
    allow_create = True
    require_login_to_create = True
    extra_filter = {}

    def get_queryset(self):
        return self.model.objects.filter(**self.extra_filter)

    def get(self, request):
        q = request.GET.get("q", "").strip()
        qs = self.get_queryset()
        if q:
            qs = qs.filter(**{f"{self.search_field}__icontains": q})
        return JsonResponse({"results": [{"value": o.pk, "text": str(o)} for o in qs[:20]]})

    def post(self, request):
        if not self.allow_create:
            return HttpResponseForbidden()
        if self.require_login_to_create and not request.user.is_authenticated:
            return JsonResponse({"error": "برای افزودن باید وارد شوید"}, status=403)
        try:
            text = json.loads(request.body or "{}").get("text", "").strip()
        except json.JSONDecodeError:
            text = ""
        if not text:
            return JsonResponse({"error": "خالی"}, status=400)
        obj, _ = self.get_queryset().get_or_create(**{self.create_field: text})
        return JsonResponse({"value": obj.pk, "text": str(obj)})
