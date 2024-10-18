from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import MockedTokenPermission
from drf_yasg import openapi

from main_api.main_api.ml_model.chatbot import Chatbot
from main_api.main_api.ml_model.random_forest_classifier import RandomForestClassifier


class LoansPredictionView(APIView):
    permission_classes = [MockedTokenPermission]

    def get(self,
            request):

        clf = RandomForestClassifier()

        prediction, data = clf.predict()

        tree_rules = clf.get_tree_rules()

        chatbot = Chatbot()

        response = chatbot.get_response(prediction=prediction,
                                        data=data,
                                        tree_rules=tree_rules)

        return Response({
            "message": response,
        })


class LoansPredictionView(APIView):
    permission_classes = [MockedTokenPermission]

    @swagger_auto_schema(
        operation_summary="Predict the loan amount",
        operation_description="Predict the loan amount for a given customer (our only customer for now). "
                              "Pass Authorization header with a Bearer token.",
        responses={200: "The predicted loan amount"}
    )
    def get(self, request):
        return Response({
            "message": "Hello, world!",
        })


class MainBalanceManyAccounts(APIView):
    ACCOUNT_NAME = "account"
    BALANCE_NAME = "balance"

    @swagger_auto_schema(
        operation_summary="Get the balances of multiple accounts",
        operation_description="Get the balances of multiple accounts. "
                              "Pass Authorization header with a Bearer token.",
        responses={200: openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    ACCOUNT_NAME + "1": openapi.Schema(type=openapi.TYPE_STRING, example="First account"),
                    BALANCE_NAME + "1": openapi.Schema(type=openapi.TYPE_INTEGER, example=5836482),
                    ACCOUNT_NAME + "2": openapi.Schema(type=openapi.TYPE_STRING, example="Second account"),
                    BALANCE_NAME + "2": openapi.Schema(type=openapi.TYPE_INTEGER, example=15104856),
                    ACCOUNT_NAME + "3": openapi.Schema(type=openapi.TYPE_STRING, example="Third account"),
                    BALANCE_NAME + "3": openapi.Schema(type=openapi.TYPE_INTEGER, example=55536433),
                    ACCOUNT_NAME + "4": openapi.Schema(type=openapi.TYPE_STRING, example="Fourth account"),
                    BALANCE_NAME + "4": openapi.Schema(type=openapi.TYPE_INTEGER, example=1536433),
                    ACCOUNT_NAME + "5": openapi.Schema(type=openapi.TYPE_STRING, example="Fifth account"),
                    BALANCE_NAME + "5": openapi.Schema(type=openapi.TYPE_INTEGER, example=32957611),
                    ACCOUNT_NAME + "6": openapi.Schema(type=openapi.TYPE_STRING, example="Sixth account"),
                    BALANCE_NAME + "6": openapi.Schema(type=openapi.TYPE_INTEGER, example=13954414),
                    ACCOUNT_NAME + "7": openapi.Schema(type=openapi.TYPE_STRING, example="Seventh account"),
                    BALANCE_NAME + "7": openapi.Schema(type=openapi.TYPE_INTEGER, example=55957001),
                },
            )
        )}
    )
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
