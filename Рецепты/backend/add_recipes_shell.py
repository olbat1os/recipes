import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

def add_recipes():
    # Очищаем все рецепты
    Recipe.objects.all().delete()
    
    # Получаем категории
    pervye = Category.objects.get(slug='pervye-blyuda')
    vtorye = Category.objects.get(slug='vtorye-blyuda')
    salaty = Category.objects.get(slug='salaty')
    zakuski = Category.objects.get(slug='zakuski')
    vypechka = Category.objects.get(slug='vypechka')
    
    # Добавляем рецепты в категорию "Первые блюда"
    Recipe.objects.create(
        title='Борщ классический',
        slug='borsch-klassicheskij',
        description='Традиционный украинский борщ с наваристым бульоном и свеклой',
        cooking_time=120,
        servings=6,
        category=pervye,
        ingredients='500г говядины\n2 свеклы\n2 картофелины\n1 морковь\n1 луковица\n2 помидора\n200г капусты\nСоль, перец по вкусу',
        instructions='Сварить мясной бульон\nНарезать овощи\nОбжарить свеклу и морковь\nДобавить овощи в бульон\nВарить до готовности'
    )
    
    Recipe.objects.create(
        title='Куриный суп с вермишелью',
        slug='kurinyj-sup-s-vermishelyu',
        description='Легкий и вкусный суп с курицей и вермишелью',
        cooking_time=60,
        servings=4,
        category=pervye,
        ingredients='400г куриного филе\n100г вермишели\n1 морковь\n1 луковица\n2 картофелины\nСоль, перец по вкусу',
        instructions='Сварить куриный бульон\nНарезать овощи\nДобавить вермишель\nВарить до готовности'
    )
    
    # Добавляем рецепты в категорию "Вторые блюда"
    Recipe.objects.create(
        title='Жаркое по-домашнему',
        slug='zharkoe-po-domashnemu',
        description='Сочное мясо с овощами в горшочке',
        cooking_time=90,
        servings=4,
        category=vtorye,
        ingredients='500г свинины\n4 картофелины\n2 моркови\n1 луковица\n2 помидора\nСоль, перец по вкусу',
        instructions='Нарезать мясо и овощи\nОбжарить мясо\nСложить в горшочек\nЗапекать 1 час'
    )
    
    Recipe.objects.create(
        title='Рыба запеченная с овощами',
        slug='ryba-zapechennaya-s-ovoschami',
        description='Филе рыбы с овощами в духовке',
        cooking_time=45,
        servings=2,
        category=vtorye,
        ingredients='400г филе рыбы\n2 помидора\n1 баклажан\n1 кабачок\nСоль, перец по вкусу',
        instructions='Нарезать овощи\nВыложить рыбу и овощи\nЗапекать 30 минут'
    )
    
    # Добавляем рецепты в категорию "Салаты"
    Recipe.objects.create(
        title='Цезарь с курицей',
        slug='cezar-s-kuricej',
        description='Классический салат Цезарь с куриным филе',
        cooking_time=30,
        servings=4,
        category=salaty,
        ingredients='400г куриного филе\n1 кочан салата\n100г пармезана\n100г сухариков\nСоус Цезарь\nСоль, перец по вкусу',
        instructions='Обжарить курицу\nНарезать салат\nСмешать ингредиенты\nЗаправить соусом'
    )
    
    Recipe.objects.create(
        title='Греческий салат',
        slug='grecheskij-salat',
        description='Традиционный греческий салат с фетой',
        cooking_time=20,
        servings=4,
        category=salaty,
        ingredients='4 помидора\n1 огурец\n1 красный лук\n100г маслин\n200г феты\nОливковое масло\nСоль, перец по вкусу',
        instructions='Нарезать овощи\nДобавить фету и маслины\nЗаправить маслом'
    )
    
    # Добавляем рецепты в категорию "Закуски"
    Recipe.objects.create(
        title='Брускетты с томатами',
        slug='brusketti-s-tomatami',
        description='Итальянские тосты с помидорами и базиликом',
        cooking_time=20,
        servings=4,
        category=zakuski,
        ingredients='4 ломтика хлеба\n4 помидора\nБазилик\nЧеснок\nОливковое масло\nСоль, перец по вкусу',
        instructions='Поджарить хлеб\nНатереть чесноком\nВыложить помидоры\nУкрасить базиликом'
    )
    
    Recipe.objects.create(
        title='Домашние чипсы',
        slug='domashnie-chipsy',
        description='Хрустящие картофельные чипсы',
        cooking_time=30,
        servings=4,
        category=zakuski,
        ingredients='4 картофелины\nРастительное масло\nСоль, перец по вкусу',
        instructions='Нарезать картофель\nОбжарить в масле\nПосыпать специями'
    )
    
    # Добавляем рецепты в категорию "Выпечка"
    Recipe.objects.create(
        title='Шарлотка с яблоками',
        slug='sharlotka-s-yablokami',
        description='Классический яблочный пирог',
        cooking_time=60,
        servings=6,
        category=vypechka,
        ingredients='4 яйца\n1 стакан сахара\n1 стакан муки\n4 яблока\nЩепотка соли',
        instructions='Взбить яйца с сахаром\nДобавить муку\nНарезать яблоки\nВыпекать 40 минут'
    )
    
    Recipe.objects.create(
        title='Булочки с корицей',
        slug='bulochki-s-koricej',
        description='Сладкие булочки с корицей и сахарной глазурью',
        cooking_time=90,
        servings=12,
        category=vypechka,
        ingredients='500г муки\n250мл молока\n50г дрожжей\n100г сахара\n2 яйца\nКорица\nСоль',
        instructions='Замесить тесто\nНастоять 1 час\nСформировать булочки\nВыпекать 20 минут'
    )
    
    print('Все рецепты успешно добавлены!')

if __name__ == '__main__':
    add_recipes() 