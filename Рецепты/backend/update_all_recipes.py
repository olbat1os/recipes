import os
import django
from django.utils.text import slugify
import uuid

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def update_all_recipes():
    # Очищаем все рецепты
    Recipe.objects.all().delete()
    print("Все существующие рецепты удалены")
    
    # Получаем категории
    categories = {
        'pervye': Category.objects.get(slug='pervye-blyuda'),
        'vtorye': Category.objects.get(slug='vtorye-blyuda'),
        'salaty': Category.objects.get(slug='salaty'),
        'zakuski': Category.objects.get(slug='zakuski'),
        'vypechka': Category.objects.get(slug='vypechka')
    }
    
    # Список всех рецептов
    all_recipes = [
        # Первые блюда
        {
            'title': 'Борщ классический',
            'description': 'Традиционный украинский борщ с наваристым бульоном и свеклой',
            'category': 'pervye',
            'cooking_time': 120,
            'servings': 6,
            'ingredients': '500г говядины\n2 свеклы\n2 картофелины\n1 морковь\n1 луковица\n2 помидора\n200г капусты\nСоль, перец по вкусу',
            'instructions': 'Сварить мясной бульон\nНарезать овощи\nОбжарить свеклу и морковь\nДобавить овощи в бульон\nВарить до готовности'
        },
        {
            'title': 'Куриный суп с вермишелью',
            'description': 'Легкий и вкусный суп с курицей и вермишелью',
            'category': 'pervye',
            'cooking_time': 60,
            'servings': 4,
            'ingredients': '400г куриного филе\n100г вермишели\n1 морковь\n1 луковица\n2 картофелины\nСоль, перец по вкусу',
            'instructions': 'Сварить куриный бульон\nНарезать овощи\nДобавить вермишель\nВарить до готовности'
        },
        {
            'title': 'Солянка сборная',
            'description': 'Наваристый суп с различными видами мяса и солеными огурцами',
            'category': 'pervye',
            'cooking_time': 90,
            'servings': 6,
            'ingredients': '300г говядины\n200г колбасы\n200г ветчины\n2 соленых огурца\n1 луковица\n2 помидора\nСоль, перец по вкусу',
            'instructions': 'Сварить мясной бульон\nНарезать мясные продукты\nДобавить огурцы и помидоры\nВарить до готовности'
        },
        
        # Вторые блюда
        {
            'title': 'Жаркое по-домашнему',
            'description': 'Сочное мясо с овощами в горшочке',
            'category': 'vtorye',
            'cooking_time': 90,
            'servings': 4,
            'ingredients': '500г свинины\n4 картофелины\n2 моркови\n1 луковица\n2 помидора\nСоль, перец по вкусу',
            'instructions': 'Нарезать мясо и овощи\nОбжарить мясо\nСложить в горшочек\nЗапекать 1 час'
        },
        {
            'title': 'Рыба запеченная с овощами',
            'description': 'Филе рыбы с овощами в духовке',
            'category': 'vtorye',
            'cooking_time': 45,
            'servings': 2,
            'ingredients': '400г филе рыбы\n2 помидора\n1 баклажан\n1 кабачок\nСоль, перец по вкусу',
            'instructions': 'Нарезать овощи\nВыложить рыбу и овощи\nЗапекать 30 минут'
        },
        {
            'title': 'Паста карбонара',
            'description': 'Классическая итальянская паста с беконом и яйцом',
            'category': 'vtorye',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': '400г спагетти\n200г бекона\n4 яйца\n100г пармезана\nЧерный перец\nСоль',
            'instructions': 'Сварить пасту\nОбжарить бекон\nСмешать с яйцами и сыром\nПриправить перцем'
        },
        
        # Салаты
        {
            'title': 'Цезарь с курицей',
            'description': 'Классический салат Цезарь с куриным филе',
            'category': 'salaty',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': '400г куриного филе\n1 кочан салата\n100г пармезана\n100г сухариков\nСоус Цезарь\nСоль, перец по вкусу',
            'instructions': 'Обжарить курицу\nНарезать салат\nСмешать ингредиенты\nЗаправить соусом'
        },
        {
            'title': 'Греческий салат',
            'description': 'Традиционный греческий салат с фетой',
            'category': 'salaty',
            'cooking_time': 20,
            'servings': 4,
            'ingredients': '4 помидора\n1 огурец\n1 красный лук\n100г маслин\n200г феты\nОливковое масло\nСоль, перец по вкусу',
            'instructions': 'Нарезать овощи\nДобавить фету и маслины\nЗаправить маслом'
        },
        {
            'title': 'Салат с тунцом',
            'description': 'Сытный салат с тунцом и овощами',
            'category': 'salaty',
            'cooking_time': 15,
            'servings': 4,
            'ingredients': '2 банки тунца\n2 помидора\n1 огурец\n1 луковица\nМайонез\nСоль, перец по вкусу',
            'instructions': 'Нарезать овощи\nСмешать с тунцом\nЗаправить майонезом'
        },
        
        # Закуски
        {
            'title': 'Брускетты с томатами',
            'description': 'Итальянские тосты с помидорами и базиликом',
            'category': 'zakuski',
            'cooking_time': 20,
            'servings': 4,
            'ingredients': '4 ломтика хлеба\n4 помидора\nБазилик\nЧеснок\nОливковое масло\nСоль, перец по вкусу',
            'instructions': 'Поджарить хлеб\nНатереть чесноком\nВыложить помидоры\nУкрасить базиликом'
        },
        {
            'title': 'Домашние чипсы',
            'description': 'Хрустящие картофельные чипсы',
            'category': 'zakuski',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': '4 картофелины\nРастительное масло\nСоль, перец по вкусу',
            'instructions': 'Нарезать картофель тонкими ломтиками\nОбжарить в масле до золотистого цвета\nПосыпать специями'
        },
        {
            'title': 'Домашние наггетсы',
            'description': 'Хрустящие куриные наггетсы',
            'category': 'zakuski',
            'cooking_time': 40,
            'servings': 4,
            'ingredients': '500г куриного филе\n2 яйца\n100г панировочных сухарей\nСоль, перец по вкусу',
            'instructions': 'Нарезать курицу на кусочки\nОбвалять в яйце и сухарях\nОбжарить до золотистого цвета'
        },
        
        # Выпечка
        {
            'title': 'Шарлотка с яблоками',
            'description': 'Классический яблочный пирог',
            'category': 'vypechka',
            'cooking_time': 60,
            'servings': 6,
            'ingredients': '4 яйца\n1 стакан сахара\n1 стакан муки\n4 яблока\nЩепотка соли',
            'instructions': 'Взбить яйца с сахаром\nДобавить муку\nНарезать яблоки\nВыпекать 40 минут'
        },
        {
            'title': 'Булочки с корицей',
            'description': 'Сладкие булочки с корицей и сахарной глазурью',
            'category': 'vypechka',
            'cooking_time': 90,
            'servings': 12,
            'ingredients': '500г муки\n250мл молока\n50г дрожжей\n100г сахара\n2 яйца\nКорица\nСоль',
            'instructions': 'Замесить тесто\nНастоять 1 час\nСформировать булочки\nВыпекать 20 минут'
        },
        {
            'title': 'Творожная запеканка',
            'description': 'Нежная творожная запеканка с изюмом',
            'category': 'vypechka',
            'cooking_time': 45,
            'servings': 6,
            'ingredients': '500г творога\n3 яйца\n100г сахара\n100г изюма\nВанилин\nСоль',
            'instructions': 'Смешать творог с яйцами и сахаром\nДобавить изюм\nВыпекать 30 минут'
        }
    ]
    
    # Добавляем все рецепты
    for recipe in all_recipes:
        try:
            # Создаем уникальный слаг, добавляя короткий UUID
            unique_id = str(uuid.uuid4())[:8]
            slug = f"{slugify(recipe['title'])}-{unique_id}"
            
            Recipe.objects.create(
                title=recipe['title'],
                slug=slug,
                description=recipe['description'],
                cooking_time=recipe['cooking_time'],
                servings=recipe['servings'],
                category=categories[recipe['category']],
                ingredients=recipe['ingredients'],
                instructions=recipe['instructions']
            )
            print(f"Добавлен рецепт в категорию '{recipe['category']}': {recipe['title']}")
        except Exception as e:
            print(f"Ошибка при добавлении рецепта {recipe['title']}: {str(e)}")
    
    print("Все рецепты успешно обновлены!")

if __name__ == '__main__':
    update_all_recipes() 