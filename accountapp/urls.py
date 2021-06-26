from django.urls import path, reverse

from accountapp import views

urlpatterns = [
    path('', views.hello_world),
]

