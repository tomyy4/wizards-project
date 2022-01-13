from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.subject_name


class Spell(models.Model):
    spell_name = models.CharField(max_length=50, blank=False)
    learnt_in = models.ForeignKey(Subject, related_name='subject', on_delete=models.CASCADE)

    def __str__(self):
        return self.spell_name


class Founder(models.Model):
    name = models.CharField(max_length=50,blank=False, unique=True)

    def __str__(self):
        return self.name


class House(models.Model):
    name = models.CharField(max_length=50,blank=False, unique=True)
    founder = models.ForeignKey(Founder, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.name


class Wizard(models.Model):
    name = models.CharField(max_length=50,blank=False, unique=True)
    house = models.ForeignKey(House, related_name='students',
    on_delete=models.CASCADE)
    spells = models.ManyToManyField(Spell, unique=True)

    def __str__(self):
        return self.name
