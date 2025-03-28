import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def check_recipes():
    categories = Category.objects.all()
    for category in categories:
        print(f"\nКатегория: {category.name}")
        recipes = Recipe.objects.filter(category=category)
        for recipe in recipes:
            print(f"- {recipe.title}")

if __name__ == '__main__':
    check_recipes() 