"""Create your models here."""

from django.db import models


class VrpLocation(models.Model):
    """Model VrpLocation definition"""

    countryCode = models.CharField(max_length=30, default="D")
    country = models.CharField(max_length=30, default="Deutschland")
    cityCode = models.CharField(max_length=30, default="B")
    city = models.CharField(max_length=30, default="Berlin")
