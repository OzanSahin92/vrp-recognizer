from django.db import models


# Create your models here.

class VrpLocation(models.Model):
    countryCode = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    cityCode = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
