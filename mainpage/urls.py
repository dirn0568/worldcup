from django.urls import path, reverse

from mainpage import views
from mainpage.views import SearchFormView, SearchDetailView

app_name='mainpage'

urlpatterns = [
    #path('', views.initial_page, name='mainpage'),
    path('', SearchFormView.as_view(), name='mainpage'),
    path('search/', SearchDetailView.as_view(), name='search'),
]

