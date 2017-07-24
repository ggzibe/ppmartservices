from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class Main(APIView):
    def get(self, request, format=None):
        return Response("Hello Django.")
