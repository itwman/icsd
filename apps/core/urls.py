from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("p/<slug:slug>/", views.page_detail, name="page"),
]
