from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class SampleViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: "OK"})
    def list(self, request):
        return Response({"message": "Hello, world!"})
