from django.db import models


# Create your models here.

class VrpLocation(models.Model):
    countryCode = models.CharField(max_length=30, default='D')
    country = models.CharField(max_length=30, default='Deutschland')
    cityCode = models.CharField(max_length=30, default='B')
    city = models.CharField(max_length=30, default='Berlin')
