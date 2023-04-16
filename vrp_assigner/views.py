"""# Create your views here."""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from vrp_assigner.models import VrpLocation
from vrp_assigner.serializers import VrpLocationSerializer


@api_view(["POST", "GET"])
def vrp_assigner(request):  # {"countryCode": "D", "cityCode": "B"}
    """View function to execute if REST-Api is called"""
    if request.method == "GET":
        return Response(
            "Hallo und Willkommen beim vrpRecognizer! Per POST request kann ermittelt werden zu welcher "
            "Stadt/Kreis das Kennzeichen gehört. Dafür müssen die jeweiligen Buchstaben für das Land "
            "(momentan nur Deutschland, also D) und für die/den Stadt/Kreis in der Form "
            '{"countryCode": "D", "cityCode": "B"} übermittelt werden!'
        )

    if request.method == "POST":
        serializer = VrpLocationSerializer(data=request.data)
        if serializer.is_valid():
            # gets the countryCode and the cityCode out of the request data
            country_code = serializer.data.get("countryCode")
            city_code = serializer.data.get("cityCode")

            # queries for corresponding data in database with countryCode and cityCode
            vrp_location = VrpLocation.objects.filter(countryCode=country_code).get(
                cityCode=city_code
            )

            # pareses found data into a dictionary and serializes it
            vrp_location_dict = {
                "country": vrp_location.country,
                "city": vrp_location.city,
            }
            response_serializer = VrpLocationSerializer(data=vrp_location_dict)

            # checks if the serialized data is valid and if it is, responds back to the request
            if response_serializer.is_valid():
                return Response(
                    response_serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                response_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
