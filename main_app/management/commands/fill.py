from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Свеча восковая в коробочке, узор "Дамасский"', 'descriptions': 'Артикул: 101', 'photo': '',
             'category': 'Узорчатые свечи', 'price': 165.2, 'date': , 'last_date': ''},
            {'name': 'Свеча восковая в коробочке, узор "Вощина"', 'descriptions': 'Артикул: 102', 'photo': '',
             'category': 'Узорчатые свечи', 'price': '', 'date': '', 'last_date': ''},
        ]
