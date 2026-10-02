from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ProjectRequestForm


def start_project(request):
    initial = {}
    if request.user.is_authenticated:
        initial = {"full_name": request.user.get_full_name(), "mobile": request.user.mobile, "email": request.user.email or ""}
    if request.GET.get("product"):
        initial["product"] = request.GET["product"]
    form = ProjectRequestForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
        obj.save()
        request.session["lead_id"] = obj.pk
        return redirect("leads:thanks")
    return render(request, "leads/start_project.html", {"form": form})


def thanks(request):
    return render(request, "leads/thanks.html")
