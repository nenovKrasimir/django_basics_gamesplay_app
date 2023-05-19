from django.urls import path, include

from django_basics_gamesplay_app.game_profile import views


urlpatterns = [
    path('create/', views.create_profile, name='create-profile')

]