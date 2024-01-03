from django.core.management import BaseCommand

from main_app.models import Product, Category
from reviews_app.models import Reviews


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Clear existing records from the models
        Category.objects.all().delete()
        Product.objects.all().delete()
        Reviews.objects.all().delete()

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
            {'name': 'Свеча восковая в коробочке, узор "Дамасский"',
             'descriptions': 'Использован генератор случайного теста. Как уже неоднократно упомянуто, акционеры крупнейших компаний представлены в исключительно положительном свете. Имеется спорная точка зрения, гласящая примерно следующее: непосредственные участники технического прогресса являются только методом политического участия и объявлены нарушающими общечеловеческие нормы этики и морали. Следует отметить, что убеждённость некоторых оппонентов однозначно фиксирует необходимость экспериментов, поражающих по своей масштабности и грандиозности.',
             'photo': 'damashkiy.jpeg',
             'category': category_one, 'price': 165.2},
            {'name': 'Свеча восковая в коробочке, узор "Вощина"',
             'descriptions': 'Использован генератор случайного теста. В своём стремлении повысить качество жизни, они забывают, что современная методология разработки однозначно фиксирует необходимость как самодостаточных, так и внешне зависимых концептуальных решений. В рамках спецификации современных стандартов, реплицированные с зарубежных источников, современные исследования неоднозначны и будут превращены в посмешище, хотя само их существование приносит несомненную пользу обществу. Есть над чем задуматься: активно развивающиеся страны третьего мира, вне зависимости от их уровня, должны быть объективно рассмотрены соответствующими инстанциями.',
             'photo': 'vochina.jpeg',
             'category': category_one, 'price': 170.8},
            {'name': 'Свеча восковая в прозрачной коробочке, "Снеговик"',
             'descriptions': 'Использован генератор случайного теста. Предварительные выводы неутешительны: существующая теория выявляет срочную потребность глубокомысленных рассуждений. Как уже неоднократно упомянуто, сторонники тоталитаризма в науке указаны как претенденты на роль ключевых факторов. А ещё базовые сценарии поведения пользователей формируют глобальную экономическую сеть и при этом — функционально разнесены на независимые элементы.',
             'photo': 'snowman.jpeg',
             'category': category_two, 'price': 133},
            {'name': 'Свеча восковая в прозрачной коробочке, яйцо "Христос Воскресе"',
             'descriptions': 'Использован генератор случайного теста. Современные технологии достигли такого уровня, что высококачественный прототип будущего проекта напрямую зависит от модели развития. Есть над чем задуматься: ключевые особенности структуры проекта могут быть функционально разнесены на независимые элементы. Однозначно, сторонники тоталитаризма в науке, вне зависимости от их уровня, должны быть ограничены исключительно образом мышления.',
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

        reviews_list = [
            {'title': 'Леди Джайна',
             'slug': 'ledi-dzajna',
             'content': 'Восковые свечи, купленные в этом магазие, излучают теплое и приглушенное свечение, создавая уютную и романтическую атмосферу в помещении. Их восковая основа имеет гладкую и блестящую текстуру, которая добавляет изысканности и элегантности. При зажигании свечи, тонкий столбик огня начинает плавно таять, заполняя воздух нежным ароматом. Они создают идеальное освещение для расслабления и наслаждения моментом, погружая вас в атмосферу спокойствия и умиротворения.',
             'photo': 'ledi_dzajna.png'},
            {'title': 'Волжин',
             'slug': 'volzhin',
             'content': 'Восковые свечи, приобретенные у случайного торговца, не вызывают особого впечатления. Они имеют обычную форму, обернуты в скромную бумагу и не привлекают внимания красочным дизайном или уникальным ароматом. Качество и длительность горения этих свечей также ничем особым не выделяется. Они служат своей основной функцией - создать некоторую атмосферу света и тепла, но не вызывают восторга или восхищения своим внешним видом или качеством изготовления.',
             'photo': 'volzhin.png'},
            {'title': 'Случайный эльф',
             'slug': 'sluchajnyij-elf',
             'content': 'Формы свечей удивительно изысканы, а их цвета великолепны и живописны. Когда свеча зажжена, ее пламя наполняет помещение магическим светом, создавая атмосферу спокойствия и умиротворения. Ароматные свечи позволяют насладиться деликатными запахами, которые придают дополнительную гармонию и расслабление. Эти восковые свечи являются идеальным дополнением для моего эльфийского дома и подарком для моих близких.',
             'photo': 'elf.png'},
        ]

        reviews_for_create = []

        for review_item in reviews_list:
            review_item['photo'] = f'reviews/{review_item["photo"]}'
            review, created = Reviews.objects.get_or_create(
                title=review_item['title'],
                slug=review_item['slug'],
                content=review_item['content'],
                photo=review_item['photo'],
            )
            if created:
                reviews_for_create.append(review)