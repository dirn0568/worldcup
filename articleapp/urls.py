from django.urls import path, reverse

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView
from startpage import views

app_name='articleapp'

urlpatterns = [
    path('article_create', ArticleCreateView.as_view(), name='article_create'),

    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),

    path('article_update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),

    path('article_delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),

]

