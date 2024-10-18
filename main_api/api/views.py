from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class LoansPredictionView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Hello, world!"
        })

