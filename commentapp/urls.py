from django.urls import path

from commentapp.views import CommentView, CommentDeleteView, CommentUpdateView

app_name = 'commentapp'

urlpatterns = [
    path('', CommentView.as_view(), name='comment'),
    path('comment_update/<int:pk>', CommentUpdateView.as_view(), name='comment_update'),
    path('comment_delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
]
