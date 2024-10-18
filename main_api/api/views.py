from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import MockedTokenPermission


class LoansPredictionView(APIView):
    permission_classes = [MockedTokenPermission]

    def get(self, request):
        return Response({
            "message": "Hello, world!",
        })


class LoansPredictionView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Hello, world!"
        })
    

class MainBalanceManyAccounts(APIView):

    ACCOUNT_NAME = "account"
    BALANCE_NAME = "balance"

    # @swagger_auto_schema(
    #     operation_description="Get bank account names and balances. Exactly 7 accounts.",
    #     responses={
    #         200: "OK",
    #     }
    # )
    def get(self, request):
        response_data = [
            {self.ACCOUNT_NAME + "1": "First account", self.BALANCE_NAME + "1": 5_836_482},
            {self.ACCOUNT_NAME + "2": "Second account", self.BALANCE_NAME + "2": 15_104_856},
            {self.ACCOUNT_NAME + "3": "Third account", self.BALANCE_NAME + "3": 55_536_433},
            {self.ACCOUNT_NAME + "4": "Fourth account", self.BALANCE_NAME + "4": 1_536_433},
            {self.ACCOUNT_NAME + "5": "Fifth account", self.BALANCE_NAME + "5": 32_957_611},
            {self.ACCOUNT_NAME + "6": "Sixth account", self.BALANCE_NAME + "6": 13_954_414},
            {self.ACCOUNT_NAME + "7": "Seventh account", self.BALANCE_NAME + "7": 55_957_001},
        ]
        return Response(response_data)
