from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from apps.academy.models import Course, Enrollment
from .gateways import GatewayError, get_gateway
from .models import Order


@login_required
def start(request, course_id):
    course = get_object_or_404(Course, pk=course_id, is_published=True)
    if course.is_free:
        return redirect("academy:enroll", slug=course.slug)
    if Enrollment.objects.filter(user=request.user, course=course, is_active=True).exists():
        return redirect("academy:learn_start", slug=course.slug)

    if request.method == "GET":
        return render(request, "payments/confirm.html", {"course": course})

    order = Order.objects.create(user=request.user, course=course, amount=course.price)
    gw = get_gateway()
    try:
        authority = gw.request(
            amount_toman=order.amount,
            callback_url=request.build_absolute_uri(reverse("payments:callback", args=[order.pk])),
            description=f"ثبت‌نام دوره‌ی {course.title}",
            mobile=request.user.mobile,
        )
    except GatewayError as e:
        order.status = "failed"
        order.save(update_fields=["status"])
        messages.error(request, str(e))
        return redirect(course)
    order.authority = authority
    order.save(update_fields=["authority"])
    return redirect(gw.pay_url(authority))


def callback(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status == "paid":
        return render(request, "payments/result.html", {"order": order, "ok": True})

    status = request.GET.get("Status")
    authority = request.GET.get("Authority", "")
    if status != "OK" or not authority or authority != order.authority:
        order.status = "canceled"
        order.save(update_fields=["status"])
        return render(request, "payments/result.html", {"order": order, "ok": False, "reason": "پرداخت لغو شد."})

    res = get_gateway().verify(order.amount, authority)
    if res["ok"]:
        order.status = "paid"
        order.ref_id = res["ref_id"]
        order.card_pan = res["card_pan"]
        order.paid_at = timezone.now()
        order.save()
        Enrollment.objects.get_or_create(user=order.user, course=order.course)
        return render(request, "payments/result.html", {"order": order, "ok": True})

    order.status = "failed"
    order.save(update_fields=["status"])
    return render(request, "payments/result.html", {"order": order, "ok": False, "reason": "تأیید پرداخت ناموفق بود. اگر مبلغی کسر شده تا ۷۲ ساعت برمی‌گردد."})
