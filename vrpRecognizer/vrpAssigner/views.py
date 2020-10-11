from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vrpRecognizer.vrpAssigner.models import VrpLocation
from vrpRecognizer.vrpAssigner.serializers import VrpLocationSerializer
from rest_framework import status


# Create your views here.

@api_view(['POST', 'GET'])
def vrpAssigner(request):
    if request.method == 'GET':
        return Response('Hallo und Willkommen beim vrpRecognizer! Per POST request kann ermittelt werden zu welcher/m '
                        'Stadt/Kreis das Kennzeichen gehört. Dafür müssen die jeweiligen Buchstaben für das Land'
                        ' (momentan nur Deutschland, also D) und für die/den Stadt/Kreis übermittelt werden!')

    elif request.method == 'POST':
        serializer = VrpLocationSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




