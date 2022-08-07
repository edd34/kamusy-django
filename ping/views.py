from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    def get(self, request, format=None):
        return Response({"status": "success"}, status=status.HTTP_200_OK)
