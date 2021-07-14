from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProjectCreateModel(models.Model):
    project = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)

    project_img = models.ImageField(upload_to='project/', null=True)
    project_title = models.CharField(max_length=30, null=True)
    project_text = models.TextField(max_length=200, null=True)