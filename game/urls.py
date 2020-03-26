from django.urls import path
from . import views
from .game_manager import GameManager

urlpatterns = [
    path('start', views.start_game),
    path('check', views.check_word),
]

# Load english dictionary on server startup
GameManager.load_english_dictionary()
