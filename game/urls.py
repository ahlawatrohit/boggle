from django.urls import path
from . import views
from .bogglecache import BoggleCache

urlpatterns = [
    path('start', views.start ),
]

bogglecache = BoggleCache()
bogglecache.load_trie_on_startup()
