import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def reset_database():
    # Удаляем все рецепты и категории
    Recipe.objects.all().delete()
    Category.objects.all().delete()
    
    # Создаем категории заново
    categories = [
        {
            'name': 'Первые блюда',
            'slug': 'pervye-blyuda',
            'description': 'Супы, борщи и другие первые блюда'
        },
        {
            'name': 'Вторые блюда',
            'slug': 'vtorye-blyuda',
            'description': 'Основные блюда из мяса, рыбы и птицы'
        },
        {
            'name': 'Салаты',
            'slug': 'salaty',
            'description': 'Разнообразные салаты на любой вкус'
        },
        {
            'name': 'Закуски',
            'slug': 'zakuski',
            'description': 'Легкие закуски и снеки'
        },
        {
            'name': 'Выпечка',
            'slug': 'vypechka',
            'description': 'Торты, пироги и другая выпечка'
        }
    ]
    
    created_categories = {}
    for cat_data in categories:
        category = Category.objects.create(**cat_data)
        created_categories[cat_data['name']] = category
        print(f'Создана категория: {category.name}')
    
    return created_categories

if __name__ == '__main__':
    print('Сброс базы данных...')
    reset_database()
    print('База данных успешно сброшена') 