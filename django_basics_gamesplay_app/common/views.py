from django.shortcuts import render

from django_basics_gamesplay_app.game_model.models import Game
from django_basics_gamesplay_app.game_profile.models import Profile


def home_page(request):
    user_registered = Profile.objects.first()
    return render(request=request, template_name='home-page.html', context={"user": user_registered})


def dashboard(request):
    games = Game.objects.all()
    user = Profile.objects.first()
    return render(request=request, template_name='dashboard.html', context={"games": games, "user": user})