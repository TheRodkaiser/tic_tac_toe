from django.urls import path
from .views import create_game, make_move, get_game, game_page

urlpatterns = [
    path('', game_page, name='game_page'),
    path('create/', create_game),
    path('move/<int:game_id>/', make_move),
    path('status/<int:game_id>/', get_game),
]
