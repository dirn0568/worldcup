from django.db import models

# Create your models here.

class WorldcupModel(models.Model):
    like_1 = models.IntegerField(default=0)
    like_2 = models.IntegerField(default=0)
    like_3 = models.IntegerField(default=0)
    like_4 = models.IntegerField(default=0)
    like_5 = models.IntegerField(default=0)
    like_6 = models.IntegerField(default=0)
    like_7 = models.IntegerField(default=0)
    like_8 = models.IntegerField(default=0)
