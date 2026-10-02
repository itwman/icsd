from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
    path("", views.game_list, name="list"),
    path("<str:slug>/", views.game_detail, name="detail"),
    path("<str:slug>/leaderboard/", views.leaderboard, name="leaderboard"),
    path("<str:slug>/score/", views.submit_score, name="score"),
]
