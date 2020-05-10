from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=300)
    steps  = models.IntegerField(default=0)
    