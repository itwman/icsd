import hashlib
import json
import re

from django.conf import settings
from django.core.cache import cache
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST

from .models import Game, Score

BAD_NAME = re.compile(r"https?://|www\.|<|>", re.I)


def _ip_hash(request):
    ip = request.META.get("HTTP_X_REAL_IP") or request.META.get("REMOTE_ADDR", "")
    return hashlib.sha256((ip + settings.SECRET_KEY[:16]).encode()).hexdigest()


def _board(game):
    return [{"player_name": s.player_name, "score": s.score} for s in game.top_scores()]


def game_list(request):
    games = Game.objects.filter(is_active=True)
    return render(request, "games/game_list.html", {"games": games})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug, is_active=True)
    return render(request, "games/game_detail.html", {
        "game": game, "seo_obj": game,
        "words_json": json.dumps(game.word_list, ensure_ascii=False) if game.engine == "wordle-fa" else "[]",
        "others": Game.objects.filter(is_active=True).exclude(pk=game.pk),
    })


@require_GET
def leaderboard(request, slug):
    game = get_object_or_404(Game, slug=slug, is_active=True)
    return JsonResponse({"leaderboard": _board(game)})


@require_POST
def submit_score(request, slug):
    game = get_object_or_404(Game, slug=slug, is_active=True)
    try:
        data = json.loads(request.body or "{}")
        score = int(data.get("score", 0))
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"message": "داده‌ی نامعتبر"}, status=400)
    name = re.sub(r"\s+", " ", str(data.get("player_name", ""))).strip()[:30]
    if not name or BAD_NAME.search(name):
        return JsonResponse({"message": "نام نامعتبر است"}, status=400)
    if score <= 0 or score > Game.MAX_SCORE.get(game.engine, 10 ** 6):
        return JsonResponse({"message": "امتیاز نامعتبر است"}, status=400)
    ip = _ip_hash(request)
    key = f"game-score:{ip}"
    if cache.get(key):
        return JsonResponse({"message": "کمی صبر کنید و دوباره ثبت کنید"}, status=429)
    cache.set(key, 1, 8)
    Score.objects.create(game=game, player_name=name, score=score, ip_hash=ip,
                         user=request.user if request.user.is_authenticated else None)
    Game.objects.filter(pk=game.pk).update(play_count=F("play_count") + 1)
    rank = game.scores.filter(is_hidden=False, score__gt=score).count() + 1
    return JsonResponse({"rank": rank, "leaderboard": _board(game)})
