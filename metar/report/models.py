from django.db import models

# Create your models here.
class DataItem(models.Model):
    station=models.CharField(max_length=30)
    last_observation=models.CharField(max_length=30)
    temperature=models.CharField(max_length=30)
    wind=models.CharField(max_length=30)