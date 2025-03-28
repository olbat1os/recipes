import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category

def check_categories():
    categories = Category.objects.all()
    print("\nСписок всех категорий:")
    for category in categories:
        print(f"ID: {category.id}, Название: {category.name}")

if __name__ == '__main__':
    check_categories() 