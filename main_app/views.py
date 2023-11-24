from django.shortcuts import render

from main_app.models import Product, Category

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
]


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'menu_catalog': Category.objects.all(),
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'main_app/index.html', context=context)


def info(request):
    context = {
        'title': 'Почему восковая свеча, а не парафиновая?',
        'menu': menu,
    }
    return render(request, 'main_app/info.html', context=context)

def about(request):
    context = {
        'title': 'Мастерская "Восковая свеча"',
        'menu': menu,
    }
    return render(request, 'main_app/about.html', context=context)

def delivery(request):
    context = {
        'title': 'Оплата и доставка',
        'menu': menu,
    }
    return render(request, 'main_app/delivery.html', context=context)

def reviews(request):
    context = {
        'title': 'Отзывы',
        'menu': menu,
    }
    return render(request, 'main_app/reviews.html', context=context)