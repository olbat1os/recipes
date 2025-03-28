from rest_framework import serializers
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'slug', 'description', 'ingredients', 'instructions', 
                 'cooking_time', 'servings', 'category', 'image', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None 