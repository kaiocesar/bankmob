from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Monopoly(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monopoly = models.ForeignKey(Monopoly, on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=5, decimal_places=2)
    steps  = models.IntegerField(default=0)
    
    def __str__(self):
       return '{} - {} - {}'.format(self.id, self.points, self.steps)

class Estate(models.Model):
    name = models.CharField(max_length=300)
    price_sell = models.DecimalField(max_digits=5, decimal_places=2)
    price_rent = models.DecimalField(max_digits=5, decimal_places=2)
    player     = models.ForeignKey(
        Player, 
        models.SET_NULL, 
        blank=True, 
        null=True, 
        default=None
    )

    def __str__(self):
        return self.name

class Board(models.Model):
    monopoly = models.ForeignKey(Monopoly, on_delete=models.CASCADE)
    estate   = models.ForeignKey(
        Estate, 
        models.SET_NULL, 
        blank=True, 
        null=True, 
        default=None
    )
    player   = models.ForeignKey(
        Player, 
        models.SET_NULL, 
        blank=True, 
        null=True, 
        default=None
    )
    status   = models.CharField(default=0, max_length=2)

    def __str__(self):
        return self.id