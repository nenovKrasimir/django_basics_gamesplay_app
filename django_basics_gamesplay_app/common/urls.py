from django.urls import path, include

from django_basics_gamesplay_app.common import views


urlpatterns = [
    path('', views.home_page, name='home-page')
]