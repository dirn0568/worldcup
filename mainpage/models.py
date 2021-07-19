from django.db import models

# Create your models here.

class SearchModel(models.Model):
    caption = models.CharField(max_length=80)