from django.core.management import BaseCommand

from main_app.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Clear existing records from the models
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_one, created_one = Category.objects.get_or_create(
            name='Узорчатые свечи',
            defaults={'descriptions': 'Узорчатые свечи'},
            slug='uzorchatye-svechi'
        )

        category_two, created_two = Category.objects.get_or_create(
            name='Рождественские свечи',
            defaults={'descriptions': 'Свечи на рождество'},
            slug='rozhdestvenskie-svechi'
        )

        category_three, created_three = Category.objects.get_or_create(
            name='Пасхальные свечи',
            defaults={'descriptions': 'Свечи на пасху'},
            slug='pashalnie-svechi'
        )

        product_list = [
            {'name': 'Свеча восковая в коробочке, узор "Дамасский"',
             'descriptions': 'Использован генератор случайного теста. Как уже неоднократно упомянуто, акционеры крупнейших компаний представлены в исключительно положительном свете. Имеется спорная точка зрения, гласящая примерно следующее: непосредственные участники технического прогресса являются только методом политического участия и объявлены нарушающими общечеловеческие нормы этики и морали. Следует отметить, что убеждённость некоторых оппонентов однозначно фиксирует необходимость экспериментов, поражающих по своей масштабности и грандиозности.',
             'photo': 'damasskij.jpeg',
             'category': category_one, 'price': 165.2,
             'slug': 'damasskiy'},
            {'name': 'Свеча восковая в коробочке, узор "Вощина"',
             'descriptions': 'Использован генератор случайного теста. В своём стремлении повысить качество жизни, они забывают, что современная методология разработки однозначно фиксирует необходимость как самодостаточных, так и внешне зависимых концептуальных решений. В рамках спецификации современных стандартов, реплицированные с зарубежных источников, современные исследования неоднозначны и будут превращены в посмешище, хотя само их существование приносит несомненную пользу обществу. Есть над чем задуматься: активно развивающиеся страны третьего мира, вне зависимости от их уровня, должны быть объективно рассмотрены соответствующими инстанциями.',
             'photo': 'voshina.jpeg',
             'category': category_one, 'price': 170.8,
             'slug': 'voshina'},
            {'name': 'Свеча восковая в прозрачной коробочке, "Снеговик"',
             'descriptions': 'Использован генератор случайного теста. Предварительные выводы неутешительны: существующая теория выявляет срочную потребность глубокомысленных рассуждений. Как уже неоднократно упомянуто, сторонники тоталитаризма в науке указаны как претенденты на роль ключевых факторов. А ещё базовые сценарии поведения пользователей формируют глобальную экономическую сеть и при этом — функционально разнесены на независимые элементы.',
             'photo': 'snegovik.jpeg',
             'category': category_two, 'price': 133,
             'slug': 'snegovik'},
            {'name': 'Свеча восковая в прозрачной коробочке, яйцо "Христос Воскресе"',
             'descriptions': 'Использован генератор случайного теста. Современные технологии достигли такого уровня, что высококачественный прототип будущего проекта напрямую зависит от модели развития. Есть над чем задуматься: ключевые особенности структуры проекта могут быть функционально разнесены на независимые элементы. Однозначно, сторонники тоталитаризма в науке, вне зависимости от их уровня, должны быть ограничены исключительно образом мышления.',
             'photo': 'hristos-voskrese.jpeg',
             'category': category_three, 'price': 154,
             'slug': 'hristos-voskrese'},
        ]

        products_for_create = []
        for product_item in product_list:
            product_item['photo'] = f'product/{product_item["photo"]}' if product_item["photo"] else ''
            product, created = Product.objects.get_or_create(
                name=product_item['name'],
                descriptions=product_item['descriptions'],
                category=product_item['category'],
                defaults={'photo': product_item['photo'], 'price': product_item['price']},
                slug=product_item['slug'],
            )
            if created:
                products_for_create.append(product)
