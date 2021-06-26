from django.urls import path, reverse

from mainpage import views

urlpatterns = [
    path('', views.initial_page),
]

