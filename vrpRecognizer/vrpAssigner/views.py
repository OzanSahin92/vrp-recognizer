from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['POST', 'GET'])
def vrpAssigner(request):
    if 'country' in request.data and 'city' in request.data:
        output = {'Country': 'Deutschland', 'City': 'Berlin'}
        return Response(output)
