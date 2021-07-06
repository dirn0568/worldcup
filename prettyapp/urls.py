from django.urls import path

from prettyapp import views
from prettyapp.views import PrettyCreationView, PrettyDetailView


app_name='prettyapp'

urlpatterns = [
    path('', PrettyCreationView.as_view(), name='create'),
    path('photo_detail/<int:pk>', PrettyDetailView.as_view(), name='photo_detail'),

    path('test', views.random_pick, name='test'),
]