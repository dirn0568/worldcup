from django.urls import path, reverse

from articleapp.views import ArticleCreateView, ArticleDetailView
from startpage import views

app_name='articleapp'

urlpatterns = [
    path('article_create', ArticleCreateView.as_view(), name='article_create'),

    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),

]

