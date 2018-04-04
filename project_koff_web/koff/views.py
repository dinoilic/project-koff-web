from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    Lists user accounts
    """
    queryset = Category.objects.all()