from django.urls import path, include

from django_basics_gamesplay_app.game_model import views


urlpatterns = [
    path('create/', views.create_game, name='create-game'),
    path('details/<int:pk>', views.details_game, name='details-game')
]