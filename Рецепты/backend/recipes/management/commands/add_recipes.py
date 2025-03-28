from django.core.management.base import BaseCommand
from django.utils.text import slugify
from recipes.models import Category, Recipe

class Command(BaseCommand):
    help = 'Добавляет рецепты в базу данных'

    def handle(self, *args, **options):
        # Очищаем существующие рецепты
        Recipe.objects.all().delete()
        self.stdout.write("Существующие рецепты удалены")

        # Получаем категории
        categories = {
            'pervye': Category.objects.get(slug='pervye-blyuda'),
            'vtorye': Category.objects.get(slug='vtorye-blyuda'),
            'salaty': Category.objects.get(slug='salaty'),
            'zakuski': Category.objects.get(slug='zakuski'),
            'vypechka': Category.objects.get(slug='vypechka')
        }

        # Список рецептов
        recipes = [
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
                'title': 'Жаркое по-домашнему',
                'description': 'Сочное мясо с овощами в горшочке',
                'category': 'vtorye',
                'cooking_time': 90,
                'servings': 4,
                'ingredients': '500г свинины\n4 картофелины\n2 моркови\n1 луковица\n2 помидора\nСоль, перец по вкусу',
                'instructions': 'Нарезать мясо и овощи\nОбжарить мясо\nСложить в горшочек\nЗапекать 1 час'
            },
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
                'title': 'Брускетты с томатами',
                'description': 'Итальянские тосты с помидорами и базиликом',
                'category': 'zakuski',
                'cooking_time': 20,
                'servings': 4,
                'ingredients': '4 ломтика хлеба\n4 помидора\nБазилик\nЧеснок\nОливковое масло\nСоль, перец по вкусу',
                'instructions': 'Поджарить хлеб\nНатереть чесноком\nВыложить помидоры\nУкрасить базиликом'
            },
            {
                'title': 'Шарлотка с яблоками',
                'description': 'Классический яблочный пирог',
                'category': 'vypechka',
                'cooking_time': 60,
                'servings': 6,
                'ingredients': '4 яйца\n1 стакан сахара\n1 стакан муки\n4 яблока\nЩепотка соли',
                'instructions': 'Взбить яйца с сахаром\nДобавить муку\nНарезать яблоки\nВыпекать 40 минут'
            }
        ]

        # Добавляем рецепты
        for recipe in recipes:
            try:
                Recipe.objects.create(
                    title=recipe['title'],
                    slug=slugify(recipe['title']),
                    description=recipe['description'],
                    cooking_time=recipe['cooking_time'],
                    servings=recipe['servings'],
                    category=categories[recipe['category']],
                    ingredients=recipe['ingredients'],
                    instructions=recipe['instructions']
                )
                self.stdout.write(f"Добавлен рецепт: {recipe['title']}")
            except Exception as e:
                self.stderr.write(f"Ошибка при добавлении рецепта {recipe['title']}: {str(e)}")

        self.stdout.write(self.style.SUCCESS("Все рецепты успешно добавлены!")) 