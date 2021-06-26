from django.urls import path, include

from endpage import views

urlpatterns = [
    path('', views.end_game),
]