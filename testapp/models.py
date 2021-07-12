from django.db import models

# Create your models here.
from commentapp.models import CommentModel


class test(models.Model):
    test1 = models.ForeignKey(CommentModel, on_delete=models.SET_NULL, related_name='test12', null=True)

    created_time = models.DateTimeField(auto_now=True)