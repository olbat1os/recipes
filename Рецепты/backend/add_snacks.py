import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

snacks = [
    {
        'title': 'Брускетты с томатами',
        'description': 'Итальянские тосты с помидорами и базиликом',
        'cooking_time': 20,
        'servings': 4,
        'ingredients': [
            '4 ломтика хлеба',
            '4 помидора',
            'Базилик',
            'Чеснок',
            'Оливковое масло',
            'Соль, перец по вкусу'
        ],
        'instructions': [
            'Поджарить хлеб',
            'Натереть чесноком',
            'Выложить помидоры',
            'Украсить базиликом'
        ]
    },
    {
        'title': 'Домашние чипсы',
        'description': 'Хрустящие картофельные чипсы',
        'cooking_time': 30,
        'servings': 4,
        'ingredients': [
            '4 картофелины',
            'Растительное масло',
            'Соль, перец по вкусу'
        ],
        'instructions': [
            'Нарезать картофель',
            'Обжарить в масле',
            'Посыпать специями'
        ]
    },
    {
        'title': 'Домашние наггетсы',
        'description': 'Хрустящие куриные наггетсы',
        'cooking_time': 40,
        'servings': 4,
        'ingredients': [
            '500г куриного филе',
            '2 яйца',
            '100г панировочных сухарей',
            'Специи',
            'Соль по вкусу'
        ],
        'instructions': [
            'Нарезать филе на кусочки',
            'Обмакнуть в яйцо',
            'Обвалять в сухарях',
            'Обжарить до золотистой корочки'
        ]
    },
    {
        'title': 'Сырные шарики',
        'description': 'Закуска из сыра и орехов',
        'cooking_time': 25,
        'servings': 6,
        'ingredients': [
            '200г плавленого сыра',
            '100г грецких орехов',
            '2 зубчика чеснока',
            'Зелень',
            'Соль, перец по вкусу'
        ],
        'instructions': [
            'Размять сыр',
            'Добавить измельченные орехи',
            'Выдавить чеснок',
            'Сформировать шарики',
            'Обвалять в зелени'
        ]
    }
]

def add_snacks():
    try:
        category = Category.objects.get(name='Закуски')
        print(f'Добавляем рецепты в категорию: Закуски (ID: {category.id})')
        
        for recipe_data in snacks:
            slug = slugify(recipe_data['title'], allow_unicode=True)
            
            # Удаляем существующий рецепт с таким же slug, если есть
            Recipe.objects.filter(slug=slug).delete()
            
            recipe = Recipe.objects.create(
                title=recipe_data['title'],
                slug=slug,
                description=recipe_data['description'],
                cooking_time=recipe_data['cooking_time'],
                servings=recipe_data['servings'],
                category=category,
                ingredients='\n'.join(recipe_data['ingredients']),
                instructions='\n'.join(recipe_data['instructions'])
            )
            print(f'Добавлен рецепт: {recipe.title}')
                
    except Category.DoesNotExist:
        print('Категория "Закуски" не найдена')

if __name__ == '__main__':
    add_snacks() 