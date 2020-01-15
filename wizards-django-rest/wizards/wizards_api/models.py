from django.db import models

# Create your models here.


class Founder(models.Model):
    name = models.CharField(max_length=50,blank=False)


class House(models.Model):
    name = models.CharField(max_length=50,blank=False)
    founder = models.ForeignKey(Founder,related_name='founder',on_delete=models.CASCADE)


class Wizard(models.Model):
    name = models.CharField(max_length=50,blank=False)
    house = models.ForeignKey(House, related_name='house',on_delete=models.CASCADE)

