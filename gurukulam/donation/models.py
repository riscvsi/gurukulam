from django.db import models

# Create your models here.

class Donation(models.Model):
    name = models.CharField(max_length=100)
    gothram = models.CharField(max_length=100, default="Nil")
    email = models.CharField(max_length=100)

    ammount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
