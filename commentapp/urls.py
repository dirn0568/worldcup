from django.urls import path

from commentapp.views import CommentView

app_name = 'commentapp'

urlpatterns = [
    path('', CommentView.as_view(), name='comment'),
]
