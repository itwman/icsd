"""صفحه‌های ویژه‌ی پنل: داشبورد، صفحه‌ساز، منو، رسانه، مرکز سئو، آمار، نقش‌ها، تاریخچه، ابزارها و جستجو."""
import json
import os
import platform
import re
import time
from datetime import timedelta
from functools import reduce
from io import StringIO
from operator import or_

import django
import jdatetime
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.core.files.storage import default_storage
from django.core.management import call_command
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Count, Q
from django.db.models.functions import TruncDate
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import get_valid_filename
from django.views.decorators.http import require_POST

from .base import panel_render, special_allowed, staff_required
from .cells import fa, jdt
from .registry import GROUPS, REGISTRY


def _need_special(request, name):
    if not special_allowed(request.user, name):
        raise PermissionDenied


def _num(n):
    return fa(f"{n:,}".replace(",", "٬"))


# ═══════════════════ داشبورد ═══════════════════
def _daily(qs, field, days=30):
    today = timezone.localdate()
    start = today - timedelta(days=days - 1)
    rows = (qs.filter(**{f"{field}__date__gte": start}).annotate(d=TruncDate(field)).values("d").annotate(n=Count("id")))
    m = {r["d"]: r["n"] for r in rows}
    return [{"d": d, "label": fa(jdatetime.date.fromgregorian(date=d).strftime("%m/%d")), "v": m.get(d, 0)}
            for d in (start + timedelta(days=i) for i in range(days))]


def _bars(series):
    peak = max([p["v"] for p in series] + [1])
    for p in series:
        p["h"] = round(p["v"] * 100 / peak, 1)
    return series, peak


@staff_required
def dashboard(request):
    from apps.academy.models import Certificate, Course, Enrollment
    from apps.analytics.models import PageView
    from apps.blog.models import Post
    from apps.games.models import Score
    from apps.leads.models import ProjectRequest
    from apps.library.models import Book
    from apps.payments.models import Order
    from apps.products.models import Product
    from apps.seo.models import NotFoundLog
    from apps.accounts.models import User

    u = request.user
    now = timezone.now()
    today = timezone.localdate()
    human = PageView.objects.exclude(device="bot")
    series, peak = _bars(_daily(human, "created_at"))
    d30 = now - timedelta(days=30)
    kpis = [
        {"t": "بازدید امروز", "v": _num(human.filter(created_at__date=today).count()), "i": "eye", "c": "sabz"},
        {"t": "بازدید ۳۰ روز", "v": _num(human.filter(created_at__gte=d30).count()), "i": "bars", "c": "firoozeh"},
        {"t": "بازدیدکننده‌ی یکتا (۳۰ روز)", "v": _num(human.filter(created_at__gte=d30).values("ip_hash").distinct().count()), "i": "users", "c": "zaferan"},
        {"t": "درخواست پروژه‌ی جدید", "v": _num(ProjectRequest.objects.filter(status="new").count()), "i": "inbox", "c": "golab",
         "url": REGISTRY["leads"].list_url() + "?f_status=new" if REGISTRY["leads"].can_view(u) else ""},
        {"t": "ثبت‌نام آکادمی (۳۰ روز)", "v": _num(Enrollment.objects.filter(created_at__gte=d30).count()), "i": "school", "c": "sabz"},
        {"t": "کاربر جدید (۳۰ روز)", "v": _num(User.objects.filter(date_joined__gte=d30).count()), "i": "user", "c": "firoozeh"},
        {"t": "گواهینامه‌ی صادرشده", "v": _num(Certificate.objects.count()), "i": "award", "c": "zaferan"},
        {"t": "فروش ۳۰ روز (تومان)", "v": _num(sum(Order.objects.filter(status="paid", paid_at__gte=d30).values_list("amount", flat=True))), "i": "cart", "c": "golab"},
    ]
    content = [
        ("نوشته", Post.objects.count(), "posts"), ("دوره", Course.objects.count(), "courses"),
        ("محصول", Product.objects.count(), "products"), ("کتاب", Book.objects.count(), "books"),
        ("امتیاز بازی", Score.objects.count(), "scores"), ("کاربر", User.objects.count(), "accounts-user"),
    ]
    content = [{"t": t, "v": _num(n), "url": REGISTRY[k].list_url()} for t, n, k in content if REGISTRY[k].can_view(u)]
    top_pages = (human.filter(created_at__gte=d30).values("path").annotate(n=Count("id")).order_by("-n")[:8])
    todo = []
    from apps.core.models import SiteSettings
    if REGISTRY["posts"].can_view(u):
        drafts = Post.objects.filter(is_published=False).count()
        if drafts:
            todo.append((f"{_num(drafts)} نوشته‌ی منتشرنشده", REGISTRY["posts"].list_url() + "?f_is_published=0"))
    if REGISTRY["404"].can_view(u):
        nf = NotFoundLog.objects.filter(resolved=False, hits__gte=3).count()
        if nf:
            todo.append((f"{_num(nf)} آدرس پرتکرار ۴۰۴ بدون ریدایرکت", REGISTRY["404"].list_url() + "?f_resolved=0"))
    if REGISTRY["leads"].can_view(u):
        newleads = ProjectRequest.objects.filter(status="new").count()
        if newleads:
            todo.append((f"{_num(newleads)} درخواست پروژه منتظر تماس", REGISTRY["leads"].list_url() + "?f_status=new"))
    if REGISTRY["settings"].perm(u, "change"):
        s = SiteSettings.load()
        if not s.logo:
            todo.append(("لوگوی سایت آپلود نشده است", REGISTRY["settings"].list_url()))
        if not s.default_og_image:
            todo.append(("تصویر پیش‌فرض اشتراک‌گذاری (OG) تعیین نشده", REGISTRY["settings"].list_url()))

    quick = []
    for key, t in (("posts", "نوشته‌ی جدید"), ("courses", "دوره‌ی جدید"), ("products", "محصول جدید"), ("books", "کتاب جدید"),
                   ("pages", "صفحه‌ی جدید"), ("customers", "مشتری جدید")):
        r = REGISTRY[key]
        if r.perm(u, "add"):
            quick.append({"t": t, "url": r.add_url(), "i": r.icon})

    return panel_render(request, "panel/dashboard.html", {
        "kpis": kpis, "series": series, "peak": _num(peak), "content": content,
        "top_pages": [{"path": p["path"], "n": _num(p["n"])} for p in top_pages],
        "leads": ProjectRequest.objects.order_by("-created_at")[:6] if REGISTRY["leads"].can_view(u) else [],
        "activity": LogEntry.objects.select_related("user", "content_type").order_by("-action_time")[:8] if u.is_superuser else [],
        "todo": todo, "quick": quick, "greet": _greet(),
        "can": {"analytics": special_allowed(u, "analytics"), "builder": special_allowed(u, "home_builder"),
                "leads": REGISTRY["leads"].can_view(u)},
        "today": _jtoday(),
    }, active="dashboard")


J_DAYS = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یکشنبه"]
J_MONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


def _jtoday():
    d = timezone.localdate()
    j = jdatetime.date.fromgregorian(date=d)
    return f"{J_DAYS[d.weekday()]} {fa(j.day)} {J_MONTHS[j.month - 1]} {fa(j.year)}"


def _greet():
    h = timezone.localtime().hour
    return "صبح بخیر" if 5 <= h < 12 else "ظهر بخیر" if h < 16 else "عصر بخیر" if h < 20 else "شب بخیر"


# ═══════════════════ صفحه‌ساز ═══════════════════
@staff_required
def home_builder(request):
    _need_special(request, "home_builder")
    from apps.core.models import HomeSection
    r = REGISTRY["home-sections"]
    if request.method == "POST" and request.POST.get("add"):
        if not r.perm(request.user, "add"):
            raise PermissionDenied
        key = request.POST["add"]
        if key not in dict(HomeSection.KEYS):
            raise Http404
        last = HomeSection.objects.order_by("-order").first()
        s = HomeSection.objects.create(key=key, title=dict(HomeSection.KEYS)[key], order=(last.order + 10 if last else 10))
        messages.success(request, "بخش اضافه شد؛ عنوان و متنش را تنظیم کنید.")
        return redirect(r.edit_url(s))
    sections = list(HomeSection.objects.all())
    for s in sections:
        s.edit = r.edit_url(s)
        s.toggle = r.url("toggle", s.pk, "is_active")
        s.delete = r.url("delete", s.pk)
    return panel_render(request, "panel/home_builder.html", {
        "sections": sections, "kinds": HomeSection.KEYS, "r": r,
        "settings_url": REGISTRY["settings"].list_url(), "can_add": r.perm(request.user, "add"),
        "can_delete": r.perm(request.user, "delete"),
    }, active="home_builder")


# ═══════════════════ منو و فوتر ═══════════════════
@staff_required
def menu(request):
    _need_special(request, "menu")
    from apps.core.models import NavLink, Page
    r = REGISTRY["menu-items"]
    if request.method == "POST":
        act = request.POST.get("act")
        if act == "add" and r.perm(request.user, "add"):
            t, u = request.POST.get("title", "").strip(), request.POST.get("url", "").strip()
            if t and u:
                last = NavLink.objects.order_by("-order").first()
                NavLink.objects.create(title=t[:60], url=u[:200], new_tab=bool(request.POST.get("new_tab")),
                                       order=(last.order + 10 if last else 10))
                messages.success(request, "آیتم منو اضافه شد.")
        elif act == "save" and r.perm(request.user, "change"):
            for link in NavLink.objects.all():
                t = request.POST.get(f"title_{link.pk}")
                u = request.POST.get(f"url_{link.pk}")
                if t is not None and u is not None and t.strip() and u.strip():
                    link.title, link.url = t.strip()[:60], u.strip()[:200]
                    link.new_tab = bool(request.POST.get(f"tab_{link.pk}"))
                    link.save()
            messages.success(request, "منو ذخیره شد.")
        elif act == "delete" and r.perm(request.user, "delete"):
            NavLink.objects.filter(pk=request.POST.get("pk")).delete()
            messages.success(request, "آیتم حذف شد.")
        return redirect("panel:menu")
    links = list(NavLink.objects.all())
    for link in links:
        link.toggle = r.url("toggle", link.pk, "is_active")
    pr = REGISTRY["pages"]
    pages = list(Page.objects.all())
    for p in pages:
        p.toggle = pr.url("toggle", p.pk, "show_in_footer")
        p.edit = pr.edit_url(p)
    suggest = [("خانه", "/"), ("محصولات", "/products/"), ("آکادمی", "/courses/"), ("مقالات", "/blog/"), ("کتابخانه", "/library/"),
               ("بازی", "/games/"), ("تیم ما", "/team/"), ("مشتریان", "/customers/"), ("شروع پروژه", "/start-project/")]
    return panel_render(request, "panel/menu.html", {"links": links, "pages": pages, "suggest": suggest, "r": r,
                                                     "settings_url": REGISTRY["settings"].list_url()}, active="menu")


# ═══════════════════ کتابخانه‌ی رسانه ═══════════════════
MEDIA_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".pdf", ".zip", ".epub", ".docx", ".xlsx", ".pptx",
             ".mp4", ".webm", ".mp3", ".txt", ".csv"}
IMG = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}
SVG_BAD = re.compile(rb"<\s*script|<\s*foreignObject|\son[a-z]+\s*=|javascript:|<!ENTITY", re.I)


def _safe_rel(rel):
    root = os.path.realpath(settings.MEDIA_ROOT)
    full = os.path.realpath(os.path.join(root, (rel or "").lstrip("/")))
    if full != root and not full.startswith(root + os.sep):
        raise PermissionDenied
    return root, full


def _human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def _media_items(folder, q="", kind=""):
    root, full = _safe_rel(folder)
    dirs, files = [], []
    if q:
        for base, ds, fs in os.walk(full):
            ds[:] = [d for d in ds if not d.startswith(".")]
            for f in fs:
                if q.lower() in f.lower():
                    files.append(os.path.join(base, f))
            if len(files) > 600:
                break
    elif os.path.isdir(full):
        for e in sorted(os.scandir(full), key=lambda e: (not e.is_dir(), e.name.lower())):
            if e.name.startswith("."):
                continue
            (dirs if e.is_dir() else files).append(e.path)
    out = []
    for p in files:
        ext = os.path.splitext(p)[1].lower()
        if kind == "image" and ext not in IMG or kind == "doc" and ext in IMG:
            continue
        try:
            st = os.stat(p)
        except OSError:
            continue
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        out.append({"name": os.path.basename(p), "rel": rel, "url": settings.MEDIA_URL + rel, "ext": ext.lstrip("."),
                    "img": ext in IMG, "size": _human(st.st_size), "mtime": st.st_mtime,
                    "date": jdt(timezone.datetime.fromtimestamp(st.st_mtime, tz=timezone.get_current_timezone()))})
    if q:
        out.sort(key=lambda x: -x["mtime"])
    return [{"name": os.path.basename(d), "rel": os.path.relpath(d, root).replace(os.sep, "/")} for d in dirs], out


@staff_required
def media(request):
    _need_special(request, "media")
    folder = request.GET.get("dir", "").strip("/")
    q = request.GET.get("q", "").strip()
    kind = request.GET.get("kind", "")
    dirs, files = _media_items(folder, q, kind)
    page = Paginator(files, 60).get_page(request.GET.get("page"))
    crumbs, acc = [], ""
    for part in [p for p in folder.split("/") if p]:
        acc = f"{acc}/{part}".strip("/")
        crumbs.append((part, acc))
    if request.GET.get("format") == "json":
        return JsonResponse({"dirs": dirs, "files": [{k: v for k, v in f.items() if k != "mtime"} for f in page.object_list],
                             "pages": page.paginator.num_pages, "page": page.number, "dir": folder})
    return panel_render(request, "panel/media.html", {"dirs": dirs, "page": page, "folder": folder, "crumbs": crumbs, "q": q,
                                                      "kind": kind, "can_delete": request.user.is_superuser}, active="media")


@staff_required
@require_POST
def media_upload(request):
    _need_special(request, "media")
    folder = request.POST.get("dir", "").strip("/") or timezone.localdate().strftime("uploads/%Y/%m")
    _safe_rel(folder)
    saved, errors = [], []
    for f in request.FILES.getlist("files"):
        ext = os.path.splitext(f.name)[1].lower()
        if ext not in MEDIA_EXT:
            errors.append(f"{f.name}: این نوع فایل مجاز نیست")
            continue
        if f.size > 50 * 1024 * 1024:
            errors.append(f"{f.name}: بیشتر از ۵۰ مگابایت")
            continue
        if ext == ".svg":
            head = f.read()
            f.seek(0)
            if SVG_BAD.search(head):
                errors.append(f"{f.name}: SVG دارای اسکریپت است")
                continue
        name = default_storage.save(f"{folder}/{get_valid_filename(f.name)}", f)
        saved.append({"rel": name, "url": default_storage.url(name), "name": os.path.basename(name), "img": ext in IMG})
    if request.headers.get("x-requested-with") == "fetch":
        return JsonResponse({"saved": saved, "errors": errors})
    for e in errors:
        messages.error(request, e)
    if saved:
        messages.success(request, f"{len(saved)} فایل آپلود شد.")
    return redirect(f"{request.path.replace('upload/', '')}?dir={folder}")


@staff_required
@require_POST
def media_delete(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    rel = request.POST.get("rel", "")
    root, full = _safe_rel(rel)
    if os.path.isfile(full):
        os.remove(full)
        messages.success(request, "فایل حذف شد.")
    elif os.path.isdir(full) and full != root and not os.listdir(full):
        os.rmdir(full)
        messages.success(request, "پوشه‌ی خالی حذف شد.")
    else:
        messages.error(request, "فقط فایل یا پوشه‌ی خالی را می‌توان حذف کرد.")
    return redirect(request.POST.get("back") or "panel:media")


@staff_required
@require_POST
def media_mkdir(request):
    _need_special(request, "media")
    parent = request.POST.get("dir", "").strip("/")
    name = get_valid_filename(request.POST.get("name", "").strip())
    if not name:
        return redirect("panel:media")
    _, full = _safe_rel(f"{parent}/{name}".strip("/"))
    os.makedirs(full, exist_ok=True)
    return redirect(f"/panel/media/?dir={parent + '/' if parent else ''}{name}")


# ═══════════════════ مرکز سئو ═══════════════════
SEO_KEYS = ["posts", "pages", "products", "courses", "team", "books", "games"]


@staff_required
def seo_center(request):
    _need_special(request, "seo")
    from apps.seo.analysis import analyze_obj
    from apps.seo.models import NotFoundLog, Redirect
    kind = request.GET.get("type", "")
    rows, total, buckets = [], 0, {"ok": 0, "mid": 0, "bad": 0}
    for key in SEO_KEYS:
        r = REGISTRY[key]
        if kind and kind != key or not r.can_view(request.user):
            continue
        for obj in r.queryset(request):
            score, checks = analyze_obj(obj, r.seo["body"], r.seo["title"])
            tone = "ok" if score >= 75 else "mid" if score >= 50 else "bad"
            buckets[tone] += 1
            total += score
            rows.append({"obj": obj, "r": r, "score": score, "tone": tone, "edit": r.edit_url(obj),
                         "issues": [m for st, m in checks if st == "bad"][:3], "noindex": obj.noindex,
                         "kw": obj.focus_keyword})
    rows.sort(key=lambda x: x["score"])
    n = len(rows)
    if request.method == "POST" and request.POST.get("act") == "indexnow":
        from apps.core.models import SiteSettings
        from apps.seo.indexnow import ping
        if not SiteSettings.load().indexnow_key:
            messages.error(request, "اول در تنظیمات سایت ← فوتر و سئو، «کلید IndexNow» را وارد کنید.")
        else:
            urls = [x["r"].view_on_site(x["obj"]) for x in rows if not x["noindex"]]
            ping([u for u in urls if u][:9000])
            messages.success(request, f"{len(urls)} آدرس برای Bing و Yandex ارسال شد.")
        return redirect("panel:seo")
    return panel_render(request, "panel/seo.html", {
        "rows": rows, "avg": round(total / n) if n else 0, "n": n, "buckets": buckets, "type": kind,
        "types": [(k, REGISTRY[k].title) for k in SEO_KEYS],
        "redirects": Redirect.objects.count(), "nf": NotFoundLog.objects.filter(resolved=False).count(),
    }, active="seo")


# ═══════════════════ آمار ═══════════════════
@staff_required
def analytics(request):
    _need_special(request, "analytics")
    from apps.analytics.models import PageView
    days = int(request.GET.get("days", 30)) if request.GET.get("days", "30").isdigit() else 30
    days = max(7, min(days, 365))
    since = timezone.now() - timedelta(days=days)
    human = PageView.objects.exclude(device="bot")
    rng = human.filter(created_at__gte=since)
    series, peak = _bars(_daily(human, "created_at", days))
    refs = (rng.exclude(referrer="").values("referrer").annotate(n=Count("id")).order_by("-n")[:40])
    hosts = {}
    for r in refs:
        h = re.sub(r"^https?://(www\.)?", "", r["referrer"]).split("/")[0]
        hosts[h] = hosts.get(h, 0) + r["n"]
    devices = {d["device"] or "نامشخص": d["n"] for d in rng.values("device").annotate(n=Count("id"))}
    total = sum(devices.values()) or 1
    return panel_render(request, "panel/analytics.html", {
        "days": days, "series": series, "peak": _num(peak), "total": _num(rng.count()),
        "uniq": _num(rng.values("ip_hash").distinct().count()),
        "bots": _num(PageView.objects.filter(device="bot", created_at__gte=since).count()),
        "pages": [{"path": p["path"], "n": _num(p["n"])} for p in rng.values("path").annotate(n=Count("id")).order_by("-n")[:25]],
        "refs": [(h, _num(n)) for h, n in sorted(hosts.items(), key=lambda x: -x[1])[:15]],
        "devices": [{"name": {"mobile": "موبایل", "desktop": "رایانه"}.get(k, k), "pct": round(v * 100 / total), "n": _num(v)} for k, v in devices.items()],
    }, active="analytics")


# ═══════════════════ نقش‌ها و مجوزها ═══════════════════
ACTIONS = [("view", "دیدن"), ("add", "افزودن"), ("change", "ویرایش"), ("delete", "حذف")]


@staff_required
def roles(request):
    _need_special(request, "roles")
    groups = Group.objects.annotate(users=Count("user"), perms=Count("permissions")).order_by("name")
    return panel_render(request, "panel/roles.html", {"groups": groups}, active="roles")


@staff_required
def role_edit(request, pk=None):
    _need_special(request, "roles")
    group = get_object_or_404(Group, pk=pk) if pk else Group()
    matrix = []
    for gkey, gtitle in GROUPS:
        rows = []
        for r in REGISTRY.values():
            if r.group != gkey or r.singleton and r.key != "settings":
                continue
            perms = {p.codename: p for p in Permission.objects.filter(content_type__app_label=r.app_label,
                                                                        content_type__model=r.model_name)}
            cells = [(a, perms.get(f"{a}_{r.model_name}")) for a, _ in ACTIONS]
            rows.append({"r": r, "cells": cells})
        if rows:
            matrix.append({"title": gtitle, "rows": rows})
    current = set(group.permissions.values_list("pk", flat=True)) if group.pk else set()
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if request.POST.get("act") == "delete" and group.pk:
            group.delete()
            messages.success(request, "نقش حذف شد.")
            return redirect("panel:roles")
        if not name:
            messages.error(request, "نام نقش را وارد کنید.")
        elif Group.objects.exclude(pk=group.pk).filter(name=name).exists():
            messages.error(request, "نقشی با این نام وجود دارد.")
        else:
            group.name = name
            group.save()
            ids = [int(x) for x in request.POST.getlist("perms") if x.isdigit()]
            group.permissions.set(Permission.objects.filter(pk__in=ids))
            messages.success(request, f"نقش «{name}» ذخیره شد ({fa(len(ids))} مجوز).")
            return redirect("panel:role_edit", pk=group.pk)
    members = group.user_set.all()[:50] if group.pk else []
    return panel_render(request, "panel/role_edit.html", {"group": group, "matrix": matrix, "current": current,
                                                          "actions": ACTIONS, "members": members,
                                                          "users_url": REGISTRY["accounts-user"].list_url()}, active="roles")


# ═══════════════════ تاریخچه ═══════════════════
@staff_required
def activity(request):
    _need_special(request, "activity")
    qs = LogEntry.objects.select_related("user", "content_type").order_by("-action_time")
    if request.GET.get("user"):
        qs = qs.filter(user_id=request.GET["user"])
    page = Paginator(qs, 50).get_page(request.GET.get("page"))
    for e in page.object_list:
        r = REGISTRY.get(f"{e.content_type.app_label}-{e.content_type.model}") if e.content_type else None
        r = r or next((x for x in REGISTRY.values() if e.content_type and x.app_label == e.content_type.app_label
                       and x.model_name == e.content_type.model), None)
        e.panel_url = (r.url("edit", e.object_id) if r and not r.singleton and e.action_flag != 3 else
                       (r.list_url() if r else ""))
        e.res_title = r.title_single if r else (e.content_type.name if e.content_type else "")
    return panel_render(request, "panel/activity.html", {"page": page}, active="activity")


# ═══════════════════ ابزارها ═══════════════════
def _dir_size(path):
    total, n = 0, 0
    for base, _, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(base, f))
                n += 1
            except OSError:
                pass
    return total, n


BACKUP_APPS = ["core", "accounts", "academy", "products", "blog", "team", "leads", "payments", "seo", "library", "games", "auth.group"]


@staff_required
def tools(request):
    _need_special(request, "tools")
    if request.method == "POST":
        act = request.POST.get("act")
        if act == "cache":
            cache.clear()
            messages.success(request, "حافظه‌ی موقت (کش) پاک شد.")
        elif act == "backup":
            buf = StringIO()
            call_command("dumpdata", *BACKUP_APPS, natural_foreign=True, indent=1, stdout=buf,
                         exclude=["accounts.otp"])
            resp = HttpResponse(buf.getvalue(), content_type="application/json; charset=utf-8")
            stamp = jdatetime.datetime.now().strftime("%Y-%m-%d-%H%M")
            resp["Content-Disposition"] = f'attachment; filename="icsd-backup-{stamp}.json"'
            return resp
        elif act == "sitemap":
            from apps.core.models import SiteSettings
            from apps.seo.indexnow import ping
            ping([SiteSettings.load().site_url.rstrip("/") + "/sitemap.xml"])
            messages.success(request, "نقشه‌ی سایت برای IndexNow ارسال شد (اگر کلید تنظیم شده باشد).")
        elif act == "cleanup":
            from apps.accounts.models import OTP
            from apps.analytics.models import PageView
            n1 = OTP.objects.filter(created_at__lt=timezone.now() - timedelta(days=2)).delete()[0]
            n2 = PageView.objects.filter(device="bot", created_at__lt=timezone.now() - timedelta(days=30)).delete()[0]
            messages.success(request, f"پاک‌سازی انجام شد: {fa(n1)} کد پیامکی قدیمی و {fa(n2)} بازدید ربات‌ها.")
        return redirect("panel:tools")
    size, files = _dir_size(settings.MEDIA_ROOT)
    db = connection.vendor
    info = [("نسخه‌ی جنگو", django.get_version()), ("پایتون", platform.python_version()), ("پایگاه داده", db),
            ("حجم رسانه‌ها", f"{_human(size)} ({fa(files)} فایل)"), ("حالت DEBUG", "روشن ⚠" if settings.DEBUG else "خاموش"),
            ("منطقه‌ی زمانی", settings.TIME_ZONE)]
    return panel_render(request, "panel/tools.html", {"info": info}, active="tools")


# ═══════════════════ جستجوی سراسری ═══════════════════
@staff_required
def search(request):
    q = request.GET.get("q", "").strip()
    results = []
    if len(q) >= 2:
        for r in REGISTRY.values():
            if not r.search or not r.can_view(request.user) or r.view_perm_only:
                continue
            qs = r.queryset(request).filter(reduce(or_, [Q(**{f"{f}__icontains": q}) for f in r.search]))[:6]
            items = [(o, r.edit_url(o)) for o in qs]
            if items:
                results.append({"r": r, "items": items})
    if request.GET.get("format") == "json":
        return JsonResponse({"results": [{"group": g["r"].title, "items": [{"text": str(o)[:80], "url": u} for o, u in g["items"]]}
                                         for g in results]})
    return panel_render(request, "panel/search.html", {"q": q, "results": results})
