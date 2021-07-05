from django.urls import path, reverse

from startpage import views

app_name='game'

urlpatterns = [
    path('', views.play, name='game'),
]

