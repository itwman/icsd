from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="list"),
    path("<str:slug>/", views.product_detail, name="detail"),
    path("<str:slug>/catalog/", views.product_catalog, name="catalog"),
    path("<str:slug>/tutorials/<int:pk>/", views.tutorial_detail, name="tutorial"),
]
