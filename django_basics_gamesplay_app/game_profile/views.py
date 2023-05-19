from django.shortcuts import render, redirect

from django_basics_gamesplay_app.game_profile.forms import ProfileForm


# Create your views here.

def create_profile(request):
    form = ProfileForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('home-page')
    return render(request=request, template_name='create-profile.html', context=context)