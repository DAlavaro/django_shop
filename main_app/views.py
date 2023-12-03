from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from main_app.models import Product, Category

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
]


class MainListView(ListView):
    model = Product
    template_name = 'main_app/index.html'
    context_object_name = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context



def candles(request, pk):
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'menu_catalog': Category.objects.all(),
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'main_app/candles.html', context=context)

def candle(request, pk):
    candle = get_object_or_404(Product, id=pk)
    context = {
        'object': candle,
        'object_list': Product.objects.filter(category_id=pk),
        'menu_catalog': Category.objects.all(),
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': candle.category_id,
    }
    return render(request, 'main_app/candle.html', context=context)


class InfoListView(ListView):
    model = Product
    template_name = 'main_app/info.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Почему восковая свеча, а не парафиновая?'
        context['menu'] = menu
        return context


class AboutListView(ListView):
    model = Product
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Мастерская "Восковая свеча"'
        context['menu'] = menu
        return context


class DeliveryListView(ListView):
    model = Product
    template_name = 'main_app/delivery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Оплата и доставка'
        context['menu'] = menu
        return context


class ReviewsListView(ListView):
    model = Product
    template_name = 'main_app/reviews.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Отзывы'
        context['menu'] = menu
        return context
