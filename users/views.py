from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .data import parks
# Create your views here.

class getParks(APIView):
    def get(self, request):
        response = {
            "parks":parks,
        }

        return Response(response)
