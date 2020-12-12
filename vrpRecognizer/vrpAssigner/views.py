from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vrpRecognizer.vrpAssigner.models import VrpLocation
from vrpRecognizer.vrpAssigner.serializers import VrpLocationSerializer
from rest_framework import status


# Create your views here.

@api_view(['POST', 'GET'])
def vrpAssigner(request):  # {"countryCode": "D", "cityCode": "B"}
    if request.method == 'GET':
        return Response('Hallo und Willkommen beim vrpRecognizer! Per POST request kann ermittelt werden zu welcher '
                        'Stadt/Kreis das Kennzeichen gehört. Dafür müssen die jeweiligen Buchstaben für das Land '
                        '(momentan nur Deutschland, also D) und für die/den Stadt/Kreis in der Form '
                        '{"countryCode": "D", "cityCode": "B"} übermittelt werden!')

    elif request.method == 'POST':
        serializer = VrpLocationSerializer(data=request.data)
        if serializer.is_valid():
            # gets the countryCode and the cityCode out of the request data
            countryC = serializer.data.get("countryCode")
            cityC = serializer.data.get("cityCode")

            # queries for corresponding data in database with countryCode and cityCode
            vrpLocation = VrpLocation.objects.filter(countryCode=countryC).get(cityCode=cityC)

            # pareses found data into a dictionary and serializes it
            vrpLocationDict = {"country": vrpLocation.country, "city": vrpLocation.city}
            responseSerializer = VrpLocationSerializer(data=vrpLocationDict)

            # checks if the serialized data is valid and if it is, responds back to the request
            if responseSerializer.is_valid():
                return Response(responseSerializer.data, status=status.HTTP_201_CREATED)
            return Response(responseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
