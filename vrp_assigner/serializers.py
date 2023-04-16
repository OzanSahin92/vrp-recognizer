"""Serialize your models here"""

from rest_framework import serializers
from vrp_assigner.models import VrpLocation


class VrpLocationSerializer(serializers.ModelSerializer):
    """Serializer for vrp loccation model"""

    class Meta:
        """Meta class for serialization"""

        model = VrpLocation
        fields = ["countryCode", "country", "cityCode", "city"]
