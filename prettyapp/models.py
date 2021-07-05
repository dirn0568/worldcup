from django import forms
from django.db import models


# Create your models here.

class PrettyModel(models.Model):
    image = models.ImageField(upload_to='pretty/', null=True)
    title = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=20, unique=True, null=True)

    # def __str__(self):
    #     return f'{self.pk} : {self.title}'
