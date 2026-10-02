from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("", views.book_list, name="list"),
    path("<str:slug>/download/", views.book_download, name="download"),
    path("<str:slug>/", views.book_detail, name="detail"),
]
