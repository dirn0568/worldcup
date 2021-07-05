from django.urls import path

from prettyapp.views import PrettyCreationView, PrettyDetailView
from startpage import views

app_name='prettyapp'

urlpatterns = [
    path('', PrettyCreationView.as_view(), name='create'),
    path('photo_detail/<int:pk>', PrettyDetailView.as_view(), name='photo_detail'),
]