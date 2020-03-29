from django.http import HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import  get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view
import json
from .game_manager import GameManager

@api_view(["GET"])
def start_game(request):
    return HttpResponse(
        json.dumps(GameManager.create_new_game()),
        content_type='application/json'
    )

@api_view(["GET"])
def check_word(request):
    try:
        word = request.GET['word']
        game_id = request.GET['game_id']
    except Exception as e:
        raise Http404("Game id and word are required fields")
    return HttpResponse(
        json.dumps(GameManager.check_word(game_id, word.lower())),
        content_type='application/json'
    )

@api_view(["GET"])
def get_game_words(request):
    try:
        game_id = request.GET['game_id']
    except Exception as e:
        raise Http404("Game id is a required field")
    return HttpResponse(
        json.dumps(GameManager.get_game_words(game_id)),
        content_type='application/json'
    )

@api_view(["GET"])
def rotate_game_board(request):
    try:
        game_id = request.GET['game_id']
    except Exception as e:
        raise Http404("Game id is a required field")
    return HttpResponse(
        json.dumps(GameManager.rotate_game_grid(game_id)),
        content_type='application/json'
    )
