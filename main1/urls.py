from django.urls import path

from .views import index, game_list

urlpatterns = [
    path('home/', index, name='home'),
    path('<str:slug>/', game_list, name="game-list"),
]