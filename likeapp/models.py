from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import ArticleCreateModel


class LikeRecordModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(ArticleCreateModel, on_delete=models.CASCADE, related_name='like_record')

    class Meta:
        unique_together = ('user', 'article')