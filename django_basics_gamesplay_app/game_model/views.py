from django.shortcuts import render, redirect

from django_basics_gamesplay_app.game_model.forms import GameForm
from django_basics_gamesplay_app.game_model.models import Game


# Create your views here.


def create_game(request):
    form = GameForm(request.POST or None)
    context = {'form': form}

    if request.method == "GET":
        return render(request=request, template_name='create-game.html', context=context)

    if form.is_valid():
        form.save()
        return redirect('home-page')


def details_game(request, pk):
    game = Game.objects.filter(id=pk).first()
    context = {'game': game}
    return render(request=request, template_name='details-game.html', context=context)

def edit_game(request, pk):
    pass