from django.urls import path, reverse

from startpage import views

urlpatterns = [
    path('', views.play),
]

