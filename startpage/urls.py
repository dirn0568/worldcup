from django.urls import path, reverse

from startpage import views
from startpage.views import GameDetailView

app_name='game'

urlpatterns = [
    path('', views.play, name='game'),
    path('test2', views.test2, name='test2'),
    path('test5', views.test5, name='test5'),

    path('game_test', GameDetailView.as_view(), name='game_test'),
    path('tetris_test', views.GameTetrisView, name='tetris_test'),
    path('worldcup', views.GameWorldcupView, name='worldcup'),
]

