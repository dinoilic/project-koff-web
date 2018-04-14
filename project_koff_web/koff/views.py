from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Category
from .serializers import CategorySerializer


class CategoryList(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Lists categories
    """
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer


class CategoryDetail(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    Retrieves a category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
