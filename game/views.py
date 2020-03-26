from django.http import HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import  get_object_or_404
import json
from .game_manager import GameManager

def start_game(request):
    return HttpResponse(
        json.dumps(GameManager.create_new_game()),
        content_type='application/json'
    )

def check_word(request):
    word = request.GET['word']
    game_id = request.GET['game_id']
    print (word)
    print (game_id)
    return HttpResponse(
        json.dumps(GameManager.check_word(game_id, word.lower())),
        content_type='application/json'
    )
