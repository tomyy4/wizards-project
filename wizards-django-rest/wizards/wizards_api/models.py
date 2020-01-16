from django.db import models


class Founder(models.Model):
    name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name


class Wizard(models.Model):
    house = models.ForeignKey(House, related_name='students',on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.subject_name


class Spell(models.Model):
    learnt_in = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)
    spell_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.spell_name