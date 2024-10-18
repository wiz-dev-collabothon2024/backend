from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

appname = "api"

urlpatterns = router.urls + [
    path("loan-predict/", views.LoansPredictionView.as_view(), name="loan-predict")
]
