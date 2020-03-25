from django.urls import path
from . import views
from .game_manager import GameManager

urlpatterns = [
    path('start', views.start_game),
]

GameManager.load_english_dictionary()
