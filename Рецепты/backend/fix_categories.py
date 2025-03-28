import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def fix_categories():
    # Словарь с правильными рецептами для каждой категории
    correct_recipes = {
        'Первые блюда': [
            'Борщ классический',
            'Куриный суп с вермишелью',
            'Солянка сборная'
        ],
        'Вторые блюда': [
            'Жаркое по-домашнему',
            'Рыба запеченная с овощами',
            'Паста карбонара'
        ],
        'Салаты': [
            'Цезарь с курицей',
            'Греческий салат',
            'Салат с тунцом'
        ],
        'Закуски': [
            'Брускетты с томатами',
            'Домашние чипсы',
            'Домашние наггетсы'
        ],
        'Выпечка': [
            'Шарлотка с яблоками',
            'Булочки с корицей',
            'Творожная запеканка'
        ]
    }

    # Удаляем все существующие рецепты
    Recipe.objects.all().delete()

    # Добавляем рецепты в правильные категории
    for category_name, recipe_titles in correct_recipes.items():
        try:
            category = Category.objects.get(name=category_name)
            print(f'Добавляем рецепты в категорию: {category_name}')
            
            for title in recipe_titles:
                slug = slugify(title, allow_unicode=True)
                recipe_data = {
                    'title': title,
                    'slug': slug,
                    'description': f'Описание для {title}',
                    'cooking_time': 60,
                    'servings': 4,
                    'category': category,
                    'ingredients': 'Ингредиенты для рецепта',
                    'instructions': 'Инструкции по приготовлению'
                }
                
                recipe = Recipe.objects.create(**recipe_data)
                print(f'Добавлен рецепт: {recipe.title}')
                    
        except Category.DoesNotExist:
            print(f'Категория не найдена: {category_name}')

if __name__ == '__main__':
    fix_categories() 