from django.core.management import BaseCommand

from main_app.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_one = Category.objects.create(name='Узорчатые свечи', descriptions='Узорчатые свечи')
        category_two = Category.objects.create(name='Рождественские свечи', descriptions='Свечи на рождество')
        category_three = Category.objects.create(name='Пасхальные свечи', descriptions='Свечи на пасху')

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
            products_for_create.append(Product(**product_item))

        Product.objects.bulk_create(products_for_create)
