from django.urls import path, reverse

from mainpage import views
from mainpage.views import SearchFormView

app_name='mainpage'

urlpatterns = [
    path('', views.initial_page, name='mainpage'),
    path('search/', SearchFormView.as_view(), name='search'),
]

