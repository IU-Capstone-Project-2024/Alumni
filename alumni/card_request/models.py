from django.db import models

# Create your models here.

class Alumni(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
