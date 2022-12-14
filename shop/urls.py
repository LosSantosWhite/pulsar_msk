from django.urls import path
from rest_framework.routers import DefaultRouter
from shop.views import MyViewSet

router = DefaultRouter()

router.register("products", MyViewSet)

urlpatterns = router.urls
