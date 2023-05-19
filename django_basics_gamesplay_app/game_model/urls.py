from django.urls import path, include

from django_basics_gamesplay_app.game_model import views


urlpatterns = [
    path('create/', views.create_game, name='create-game'),
    path('details/<int:pk>', views.details_game, name='details-game'),
    path('edit/<int:pk>', views.edit_game, name='edit-game'),
    path('delete/<int:pk>', views.delete_game, name='delete-game')
]