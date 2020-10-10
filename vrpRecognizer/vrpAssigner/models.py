from django.db import models

# Create your models here.

class VrpLocation(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
