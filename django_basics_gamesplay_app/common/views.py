from django.shortcuts import render

from django_basics_gamesplay_app.game_profile.models import Profile


def home_page(request):
    user_registered = Profile.objects.first()

    return render(request=request, template_name='home-page.html', context={"user": user_registered})
