from django.core.management import BaseCommand

from main_app.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_one, created_one = Category.objects.get_or_create(
            name='Узорчатые свечи',
            defaults={'descriptions': 'Узорчатые свечи'}
        )

        category_two, created_two = Category.objects.get_or_create(
            name='Рождественские свечи',
            defaults={'descriptions': 'Свечи на рождество'}
        )

        category_three, created_three = Category.objects.get_or_create(
            name='Пасхальные свечи',
            defaults={'descriptions': 'Свечи на пасху'}
        )

        product_list = [
            {'name': 'Свеча восковая в коробочке, узор "Дамасский"', 'descriptions': 'Артикул: 101',
             'photo': 'damashkiy.jpeg',
             'category': category_one, 'price': 165.2},
            {'name': 'Свеча восковая в коробочке, узор "Вощина"', 'descriptions': 'Артикул: 102',
             'photo': 'vochina.jpeg',
             'category': category_one, 'price': 170.8},
            {'name': 'Свеча восковая в прозрачной коробочке, "Снеговик"', 'descriptions': 'Артикул: 201',
             'photo': 'snowman.jpeg',
             'category': category_two, 'price': 133},
            {'name': 'Свеча восковая в прозрачной коробочке, яйцо "Христос Воскресе"', 'descriptions': 'Артикул: 301',
             'photo': 'egg.jpeg',
             'category': category_three, 'price': 154},
        ]

        products_for_create = []
        for product_item in product_list:
            product_item['photo'] = f'product/{product_item["photo"]}' if product_item["photo"] else ''
            product, created = Product.objects.get_or_create(
                name=product_item['name'],
                descriptions=product_item['descriptions'],
                category=product_item['category'],
                defaults={'photo': product_item['photo'], 'price': product_item['price']}
            )
            if created:
                products_for_create.append(product)
