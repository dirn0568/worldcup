from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import ProjectCreateModel


class SubscribeCreateModel(models.Model):
    subscribe_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription', null=True)
    subscribe_project = models.ForeignKey(ProjectCreateModel, on_delete=models.CASCADE, related_name='subscription', null=True)

    class Meta:
        unique_together = ('subscribe_user', 'subscribe_project')