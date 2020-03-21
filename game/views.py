from django.http import HttpResponse
import json
from .game import Game

def start(request, x=0,y=0):    
    game = Game()
    return HttpResponse(json.dumps(game.start()), content_type='application/json')
