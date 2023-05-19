
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_basics_gamesplay_app.common.urls')),
    path('profile/', include('django_basics_gamesplay_app.game_profile.urls')),
    path('game/', include('django_basics_gamesplay_app.game_model.urls'))
]
