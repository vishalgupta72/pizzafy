from django.db import models

# Create your models here.

class Pizza(models.Model):
    type = models.CharField(max_length=50)
    size = models.IntegerField()