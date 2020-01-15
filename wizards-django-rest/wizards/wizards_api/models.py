from django.db import models

# Create your models here.


class Wizard(models.Model):
    name = models.CharField(max_length=50,blank=False)
    house = models.CharField(max_length=50,blank=False)


class House(models.Model):
    name = models.CharField(max_length=50,blank=False)


