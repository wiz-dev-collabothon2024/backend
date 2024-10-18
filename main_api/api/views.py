from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import MockedTokenPermission


class LoansPredictionView(APIView):
    permission_classes = [MockedTokenPermission]

    def get(self, request):
        return Response({
            "message": "Hello, world!",
        })
