import os
import django
from django.utils.text import slugify

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def add_missing_recipes():
    # Получаем категории
    zakuski = Category.objects.get(slug='zakuski')
    vypechka = Category.objects.get(slug='vypechka')
    
    # Список рецептов для категории "Закуски"
    zakuski_recipes = [
        {
            'title': 'Домашние чипсы',
            'description': 'Хрустящие картофельные чипсы',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': '4 картофелины\nРастительное масло\nСоль, перец по вкусу',
            'instructions': 'Нарезать картофель тонкими ломтиками\nОбжарить в масле до золотистого цвета\nПосыпать специями'
        },
        {
            'title': 'Домашние наггетсы',
            'description': 'Хрустящие куриные наггетсы',
            'cooking_time': 40,
            'servings': 4,
            'ingredients': '500г куриного филе\n2 яйца\n100г панировочных сухарей\nСоль, перец по вкусу',
            'instructions': 'Нарезать курицу на кусочки\nОбвалять в яйце и сухарях\nОбжарить до золотистого цвета'
        },
        {
            'title': 'Сырные шарики',
            'description': 'Хрустящие сырные шарики',
            'cooking_time': 25,
            'servings': 4,
            'ingredients': '200г твердого сыра\n100г муки\n2 яйца\n100г панировочных сухарей\nСоль, перец по вкусу',
            'instructions': 'Натереть сыр\nСформировать шарики\nОбвалять в муке, яйце и сухарях\nОбжарить до золотистого цвета'
        }
    ]
    
    # Список рецептов для категории "Выпечка"
    vypechka_recipes = [
        {
            'title': 'Шарлотка с яблоками',
            'description': 'Классический яблочный пирог',
            'cooking_time': 60,
            'servings': 6,
            'ingredients': '4 яйца\n1 стакан сахара\n1 стакан муки\n4 яблока\nЩепотка соли',
            'instructions': 'Взбить яйца с сахаром\nДобавить муку\nНарезать яблоки\nВыпекать 40 минут'
        },
        {
            'title': 'Булочки с корицей',
            'description': 'Сладкие булочки с корицей и сахарной глазурью',
            'cooking_time': 90,
            'servings': 12,
            'ingredients': '500г муки\n250мл молока\n50г дрожжей\n100г сахара\n2 яйца\nКорица\nСоль',
            'instructions': 'Замесить тесто\nНастоять 1 час\nСформировать булочки\nВыпекать 20 минут'
        },
        {
            'title': 'Творожная запеканка',
            'description': 'Нежная творожная запеканка с изюмом',
            'cooking_time': 45,
            'servings': 6,
            'ingredients': '500г творога\n3 яйца\n100г сахара\n100г изюма\nВанилин\nСоль',
            'instructions': 'Смешать творог с яйцами и сахаром\nДобавить изюм\nВыпекать 30 минут'
        }
    ]
    
    # Добавляем рецепты в категорию "Закуски"
    for recipe in zakuski_recipes:
        try:
            Recipe.objects.create(
                title=recipe['title'],
                slug=slugify(recipe['title']),
                description=recipe['description'],
                cooking_time=recipe['cooking_time'],
                servings=recipe['servings'],
                category=zakuski,
                ingredients=recipe['ingredients'],
                instructions=recipe['instructions']
            )
            print(f"Добавлен рецепт в категорию 'Закуски': {recipe['title']}")
        except Exception as e:
            print(f"Ошибка при добавлении рецепта {recipe['title']}: {str(e)}")
    
    # Добавляем рецепты в категорию "Выпечка"
    for recipe in vypechka_recipes:
        try:
            Recipe.objects.create(
                title=recipe['title'],
                slug=slugify(recipe['title']),
                description=recipe['description'],
                cooking_time=recipe['cooking_time'],
                servings=recipe['servings'],
                category=vypechka,
                ingredients=recipe['ingredients'],
                instructions=recipe['instructions']
            )
            print(f"Добавлен рецепт в категорию 'Выпечка': {recipe['title']}")
        except Exception as e:
            print(f"Ошибка при добавлении рецепта {recipe['title']}: {str(e)}")
    
    print("Все недостающие рецепты успешно добавлены!")

if __name__ == '__main__':
    add_missing_recipes() 