from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path("", views.start_project, name="start"),
    path("thanks/", views.thanks, name="thanks"),
]
