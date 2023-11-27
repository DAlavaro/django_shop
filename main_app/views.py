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

def candles(request, pk):
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'menu_catalog': Category.objects.all(),
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'main_app/candles.html', context=context)


def info(request):
    context = {
        'object_list': Product.objects.all(),
        'menu_catalog': Category.objects.all(),
        'title': 'Почему восковая свеча, а не парафиновая?',
        'menu': menu,
    }
    return render(request, 'main_app/info.html', context=context)

def about(request):
    context = {
        'object_list': Product.objects.all(),
        'menu_catalog': Category.objects.all(),
        'title': 'Мастерская "Восковая свеча"',
        'menu': menu,
    }
    return render(request, 'main_app/about.html', context=context)

def delivery(request):
    context = {
        'object_list': Product.objects.all(),
        'menu_catalog': Category.objects.all(),
        'title': 'Оплата и доставка',
        'menu': menu,
    }
    return render(request, 'main_app/delivery.html', context=context)

def reviews(request):
    context = {
        'object_list': Product.objects.all(),
        'menu_catalog': Category.objects.all(),
        'title': 'Отзывы',
        'menu': menu,
    }
    return render(request, 'main_app/reviews.html', context=context)