from django.urls import path
from . import views
from .game_manager import GameManager

urlpatterns = [
    path('start', views.start_game),
    path('check', views.check_word),
    path('result', views.get_game_words),
    path('rotate', views.rotate_game_board),
]

# Load english dictionary on server startup
GameManager.load_english_dictionary()
