from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .model_serializers import Category, CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
