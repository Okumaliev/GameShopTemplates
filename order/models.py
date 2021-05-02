from django.db import models

from main1.models import Game


class Order(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='orders')
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=55)
    city = models.CharField(max_length=44)
    email = models.EmailField(max_length=33)

    def __str__(self):
        return f'{self.email}'



