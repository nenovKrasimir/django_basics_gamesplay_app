from django.shortcuts import render, redirect

from django_basics_gamesplay_app.game_model.models import Game
from django_basics_gamesplay_app.game_profile.forms import ProfileForm
from django_basics_gamesplay_app.game_profile.models import Profile


# Create your views here.

def create_profile(request):
    form = ProfileForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('home-page')
    return render(request=request, template_name='create-profile.html', context=context)


def details_profile(request):
    total_games = Game.objects.count()
    average_rating = 0

    for game in Game.objects.all():
        average_rating += game.rating

    average_rating = average_rating/total_games if average_rating else 0

    profile = Profile.objects.first()
    context = {'user': profile, 'total_games': total_games, 'average_rating': average_rating}
    return render(request=request, template_name='details-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == "POST":
        profile.delete()
        for game in Game.objects.all():
            game.delete()

        return redirect('home-page')

    return render(request=request, template_name='delete-profile.html')


def edit_profile(request):
    profile = Profile.objects.first()
    form = ProfileForm(request.POST or None, instance=profile)
    context = {"user": profile, "form": form}

    if request.method == "GET":
        return render(request=request, template_name="edit-profile.html", context=context)

    if form.is_valid():
        form.save()
        return redirect('details-profile')
