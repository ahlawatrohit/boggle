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
