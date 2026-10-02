from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("course/<int:course_id>/", views.start, name="start"),
    path("callback/<int:order_id>/", views.callback, name="callback"),
]
