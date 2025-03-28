from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'cooking_time', 'servings')
    list_filter = ('category', 'cooking_time', 'servings')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
