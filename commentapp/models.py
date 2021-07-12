from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accountapp.models import Profile
from articleapp.models import ArticleCreateModel


class CommentModel(models.Model):
    writer = models.ForeignKey(ArticleCreateModel, on_delete=models.SET_NULL, related_name='writer', null=True)
    writer_nickname = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='writer_nickname', null=True)

    comment_text = models.TextField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)

