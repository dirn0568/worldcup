from django.urls import path

from likeapp.views import LikeArticleView

app_name='likeapp'

urlpatterns = [
    path('likes/<int:pk>', LikeArticleView.as_view(), name='article_like'),
]