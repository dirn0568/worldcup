from django.urls import path, reverse

from mainpage import views

app_name='mainpage'

urlpatterns = [
    path('', views.initial_page, name='mainpage'),
]

