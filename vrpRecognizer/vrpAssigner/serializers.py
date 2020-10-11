from vrpRecognizer.vrpAssigner.models import VrpLocation
from rest_framework import serializers


class VrpLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VrpLocation
        fields = ['countryCode', 'country', 'cityCode', 'city']
