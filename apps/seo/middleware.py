from urllib.parse import unquote

from django.db.models import F
from django.http import HttpResponseGone, HttpResponsePermanentRedirect, HttpResponseRedirect


class RedirectMiddleware:
    """روی ۴۰۴، جدول ریدایرکت را چک می‌کند (با و بدون / انتها، و decode شده‌ی فارسی)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 404:
            return response
        from .models import Redirect
        raw = request.path
        candidates = {raw, unquote(raw)}
        for p in list(candidates):
            candidates.add(p.rstrip("/") + "/" if not p.endswith("/") else p.rstrip("/") or "/")
        r = Redirect.objects.filter(old_path__in=candidates, is_active=True).first()
        if not r:
            return response
        Redirect.objects.filter(pk=r.pk).update(hits=F("hits") + 1)
        if r.status_code == 410 or not r.new_path:
            return HttpResponseGone("این صفحه حذف شده است.")
        if r.status_code == 302:
            return HttpResponseRedirect(r.new_path)
        return HttpResponsePermanentRedirect(r.new_path)
