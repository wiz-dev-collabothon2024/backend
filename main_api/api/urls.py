from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register(r"sample-endpoint", views.SampleViewSet, basename="sample-endpoint")

appname = "api"

urlpatterns = router.urls
