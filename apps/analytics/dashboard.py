"""داشبورد پنل مدیریت: آمار بازدید، درخواست‌ها، ثبت‌نام‌ها."""
from datetime import timedelta

import jdatetime
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone

FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def _fa(n):
    return f"{n:,}".replace(",", "٬").translate(FA)


def callback(request, context):
    from apps.academy.models import Enrollment
    from apps.leads.models import ProjectRequest
    from apps.payments.models import Order
    from .models import PageView

    now = timezone.now()
    today = now.date()
    d7 = now - timedelta(days=7)
    d30 = now - timedelta(days=30)
    human = PageView.objects.exclude(device="bot")

    # ۳۰ روز اخیر — برای نمودار
    daily = (human.filter(created_at__gte=d30).annotate(d=TruncDate("created_at"))
             .values("d").annotate(n=Count("id")).order_by("d"))
    series = {row["d"]: row["n"] for row in daily}
    days = [(today - timedelta(days=i)) for i in range(29, -1, -1)]
    chart = [{"label": jdatetime.date.fromgregorian(date=d).strftime("%m/%d").translate(FA),
              "value": series.get(d, 0)} for d in days]
    peak = max((p["value"] for p in chart), default=1) or 1

    top_pages = (human.filter(created_at__gte=d30).values("path")
                 .annotate(n=Count("id")).order_by("-n")[:10])

    context.update({
        "kpis": [
            {"title": "بازدید امروز", "value": _fa(human.filter(created_at__date=today).count())},
            {"title": "بازدید ۷ روز", "value": _fa(human.filter(created_at__gte=d7).count())},
            {"title": "بازدیدکننده‌ی یکتا (۳۰ روز)", "value": _fa(human.filter(created_at__gte=d30).values("ip_hash").distinct().count())},
            {"title": "درخواست پروژه‌ی جدید", "value": _fa(ProjectRequest.objects.filter(status="new").count())},
            {"title": "ثبت‌نام ۳۰ روز", "value": _fa(Enrollment.objects.filter(created_at__gte=d30).count())},
            {"title": "فروش ۳۰ روز (تومان)", "value": _fa(sum(Order.objects.filter(status="paid", paid_at__gte=d30).values_list("amount", flat=True)))},
        ],
        "chart": chart, "chart_peak": peak,
        "top_pages": [{"path": r["path"], "n": _fa(r["n"])} for r in top_pages],
        "recent_leads": ProjectRequest.objects.order_by("-created_at")[:6],
    })
    return context
