from django.db import models

class Food(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
