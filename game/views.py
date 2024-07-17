from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Game
import json

@csrf_exempt
def create_game(request):
    if request.method == 'POST':
        game = Game.objects.create()
        return JsonResponse({'game_id': game.id, 'board': game.board})

@csrf_exempt
def make_move(request, game_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        game = Game.objects.get(id=game_id)
        position = data['position']
        player = data['player']
        game.make_move(position, player)
        return JsonResponse({
            'game_id': game.id,
            'board': game.board,
            'winner': game.winner,
            'game_over': game.game_over,
            'current_turn': game.current_turn
        })

def get_game(request, game_id):
    game = Game.objects.get(id=game_id)
    return JsonResponse({
        'game_id': game.id,
        'board': game.board,
        'winner': game.winner,
        'game_over': game.game_over,
        'current_turn': game.current_turn
    })

def game_page(request):
    return render(request, 'game/index.html')
