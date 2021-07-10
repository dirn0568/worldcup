from django.db import models

# Create your models here.
from articleapp.models import ArticleCreateModel


class CommentModel(models.Model):
    writer = models.ForeignKey(ArticleCreateModel, on_delete=models.SET_NULL, related_name='writer', null=True)

    comment_text = models.TextField(max_length=100)

