from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import ProjectCreateModel


class ArticleCreateModel(models.Model):
    article = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    article_project = models.ForeignKey(ProjectCreateModel, on_delete=models.SET_NULL, related_name='article_project', null=True)

    article_img = models.ImageField(upload_to='article/', null=True)
    article_title = models.CharField(max_length=30, unique=True, null=True)
    article_text = models.TextField(max_length=200, null=True)
