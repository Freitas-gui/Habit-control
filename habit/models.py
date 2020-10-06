from django.db import models

class Habit(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    trigger = models.TextField(max_length=200)
    routine = models.TextField(max_length=200)
    reward = models.TextField(max_length=200)
    good = models.BooleanField(blank=False, null=False)