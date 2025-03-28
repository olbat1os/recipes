import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from recipes.models import Category, Recipe

recipes_data = {
    'Первые блюда': [
        {
            'title': 'Борщ классический',
            'description': 'Традиционный украинский борщ с наваристым бульоном и свеклой',
            'cooking_time': 120,
            'servings': 6,
            'ingredients': [
                '500г говядины',
                '2 свеклы',
                '2 картофелины',
                '1 морковь',
                '1 луковица',
                '2 помидора',
                '200г капусты',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Сварить мясной бульон',
                'Нарезать овощи',
                'Обжарить свеклу и морковь',
                'Добавить овощи в бульон',
                'Варить до готовности'
            ]
        },
        {
            'title': 'Куриный суп с вермишелью',
            'description': 'Легкий и вкусный суп с курицей и вермишелью',
            'cooking_time': 60,
            'servings': 4,
            'ingredients': [
                '400г куриного филе',
                '100г вермишели',
                '1 морковь',
                '1 луковица',
                '2 картофелины',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Сварить куриный бульон',
                'Нарезать овощи',
                'Добавить вермишель',
                'Варить до готовности'
            ]
        },
        {
            'title': 'Солянка сборная',
            'description': 'Наваристый суп с колбасой, мясом и солеными огурцами',
            'cooking_time': 90,
            'servings': 6,
            'ingredients': [
                '300г говядины',
                '200г колбасы',
                '100г ветчины',
                '2 соленых огурца',
                '1 луковица',
                '1 морковь',
                '2 ст.л. томатной пасты',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Сварить мясной бульон',
                'Нарезать колбасу, ветчину и огурцы',
                'Обжарить лук и морковь',
                'Добавить томатную пасту',
                'Соединить все ингредиенты',
                'Варить 15 минут'
            ]
        }
    ],
    'Вторые блюда': [
        {
            'title': 'Жаркое по-домашнему',
            'description': 'Сочное мясо с овощами в горшочке',
            'cooking_time': 90,
            'servings': 4,
            'ingredients': [
                '500г свинины',
                '4 картофелины',
                '2 моркови',
                '1 луковица',
                '2 помидора',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Нарезать мясо и овощи',
                'Обжарить мясо',
                'Сложить в горшочек',
                'Запекать 1 час'
            ]
        },
        {
            'title': 'Рыба запеченная с овощами',
            'description': 'Филе рыбы с овощами в духовке',
            'cooking_time': 45,
            'servings': 2,
            'ingredients': [
                '400г филе рыбы',
                '2 помидора',
                '1 баклажан',
                '1 кабачок',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Нарезать овощи',
                'Выложить рыбу и овощи',
                'Запекать 30 минут'
            ]
        },
        {
            'title': 'Паста карбонара',
            'description': 'Классическая итальянская паста с беконом и яйцом',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': [
                '400г спагетти',
                '200г бекона',
                '4 яйца',
                '100г пармезана',
                'Черный перец',
                'Соль по вкусу'
            ],
            'instructions': [
                'Отварить спагетти',
                'Обжарить бекон',
                'Смешать яйца с тертым сыром',
                'Соединить все ингредиенты',
                'Приправить перцем'
            ]
        }
    ],
    'Салаты': [
        {
            'title': 'Цезарь с курицей',
            'description': 'Классический салат Цезарь с куриным филе',
            'cooking_time': 30,
            'servings': 4,
            'ingredients': [
                '400г куриного филе',
                '1 кочан салата',
                '100г пармезана',
                '100г сухариков',
                'Соус Цезарь',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Обжарить курицу',
                'Нарезать салат',
                'Смешать ингредиенты',
                'Заправить соусом'
            ]
        },
        {
            'title': 'Греческий салат',
            'description': 'Традиционный греческий салат с фетой',
            'cooking_time': 20,
            'servings': 4,
            'ingredients': [
                '4 помидора',
                '1 огурец',
                '1 красный лук',
                '100г маслин',
                '200г феты',
                'Оливковое масло',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Нарезать овощи',
                'Добавить фету и маслины',
                'Заправить маслом'
            ]
        },
        {
            'title': 'Салат с тунцом',
            'description': 'Легкий салат с тунцом и овощами',
            'cooking_time': 20,
            'servings': 4,
            'ingredients': [
                '1 банка тунца',
                '2 помидора',
                '1 огурец',
                '1 красный лук',
                'Оливковое масло',
                'Соль, перец по вкусу'
            ],
            'instructions': [
                'Нарезать овощи',
                'Смешать с тунцом',
                'Заправить маслом'
            ]
        }
    ],
    'Закуски': [
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
        }
    ],
    'Выпечка': [
        {
            'title': 'Шарлотка с яблоками',
            'description': 'Классический яблочный пирог',
            'cooking_time': 60,
            'servings': 6,
            'ingredients': [
                '4 яйца',
                '1 стакан сахара',
                '1 стакан муки',
                '4 яблока',
                'Щепотка соли'
            ],
            'instructions': [
                'Взбить яйца с сахаром',
                'Добавить муку',
                'Нарезать яблоки',
                'Выпекать 40 минут'
            ]
        },
        {
            'title': 'Булочки с корицей',
            'description': 'Сладкие булочки с корицей и сахарной глазурью',
            'cooking_time': 90,
            'servings': 12,
            'ingredients': [
                '500г муки',
                '250мл молока',
                '50г дрожжей',
                '100г сахара',
                '2 яйца',
                'Корица',
                'Соль'
            ],
            'instructions': [
                'Замесить тесто',
                'Настоять 1 час',
                'Сформировать булочки',
                'Выпекать 20 минут'
            ]
        },
        {
            'title': 'Творожная запеканка',
            'description': 'Нежная творожная запеканка с изюмом',
            'cooking_time': 60,
            'servings': 6,
            'ingredients': [
                '500г творога',
                '3 яйца',
                '100г сахара',
                '100г изюма',
                '2 ст.л. манки',
                'Ванилин'
            ],
            'instructions': [
                'Смешать творог с яйцами',
                'Добавить сахар и манку',
                'Вмешать изюм',
                'Выпекать 40 минут'
            ]
        }
    ]
}

def add_all_recipes():
    # Удаляем все существующие рецепты
    Recipe.objects.all().delete()
    
    for category_name, recipes in recipes_data.items():
        try:
            category = Category.objects.get(name=category_name)
            print(f'Добавляем рецепты в категорию: {category_name}')
            
            for recipe_data in recipes:
                slug = slugify(recipe_data['title'], allow_unicode=True)
                
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
            print(f'Категория не найдена: {category_name}')
        except Exception as e:
            print(f'Ошибка при добавлении рецепта: {str(e)}')

if __name__ == '__main__':
    add_all_recipes() 