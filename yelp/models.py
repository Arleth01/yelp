from django.db import models

class Food(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)

class Customer(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(default = 0)
    phone = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)

class Order(models.Model):
    food = models.CharField(max_length = 200)
    quantity = models.CharField(max_length = 200)
    total = models.FloatField(default = 0)
    customer = models.CharField(max_length =  200)
    address = models.CharField(max_length = 200)

class restaurant(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length = 200)
