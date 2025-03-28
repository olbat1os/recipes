from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer

# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 100  # Устанавливаем большой размер страницы, чтобы получить все рецепты

    def get_queryset(self):
        queryset = Recipe.objects.all()
        category_slug = self.request.query_params.get('category', None)
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
