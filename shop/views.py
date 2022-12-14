from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from shop.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from shop.models import Product
from django.shortcuts import get_object_or_404


class MyViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["status"]
    search_fields = ["barcode", "title"]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
