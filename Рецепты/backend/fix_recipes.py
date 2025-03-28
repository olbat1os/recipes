import os
import django
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def fix_duplicates():
    # Находим дубликаты по названию и категории
    duplicates = Recipe.objects.values('title', 'category').annotate(count=Count('id')).filter(count__gt=1)
    
    for dup in duplicates:
        # Получаем все рецепты с таким названием в этой категории
        recipes = Recipe.objects.filter(title=dup['title'], category_id=dup['category'])
        
        # Оставляем первый рецепт, удаляем остальные
        first_recipe = recipes.first()
        recipes.exclude(id=first_recipe.id).delete()
        print(f"Удалены дубликаты рецепта: {first_recipe.title}")

if __name__ == '__main__':
    fix_duplicates() 