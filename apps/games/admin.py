from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Game, Score


@admin.register(Game)
class GameAdmin(ModelAdmin):
    list_display = ("title", "engine", "play_count", "is_active", "order")


@admin.register(Score)
class ScoreAdmin(ModelAdmin):
    list_display = ("player_name", "game", "score", "is_hidden", "created_at")
    list_filter = ("game", "is_hidden")
