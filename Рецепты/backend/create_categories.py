import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category

def create_categories():
    # Удаляем все существующие категории
    Category.objects.all().delete()
    
    # Список категорий для создания
    categories = [
        {
            'name': 'Первые блюда',
            'description': 'Супы, борщи и другие первые блюда',
            'slug': 'pervye-blyuda'
        },
        {
            'name': 'Вторые блюда',
            'description': 'Основные блюда из мяса, рыбы и птицы',
            'slug': 'vtorye-blyuda'
        },
        {
            'name': 'Салаты',
            'description': 'Разнообразные салаты на любой вкус',
            'slug': 'salaty'
        },
        {
            'name': 'Закуски',
            'description': 'Легкие закуски и снеки',
            'slug': 'zakuski'
        },
        {
            'name': 'Выпечка',
            'description': 'Торты, пироги и другая выпечка',
            'slug': 'vypechka'
        }
    ]
    
    # Создаем категории
    for category_data in categories:
        try:
            category = Category.objects.create(
                name=category_data['name'],
                slug=category_data['slug'],
                description=category_data['description']
            )
            print(f'Создана категория: {category.name} (ID: {category.id})')
        except Exception as e:
            print(f'Ошибка при создании категории {category_data["name"]}: {str(e)}')

if __name__ == '__main__':
    create_categories() 