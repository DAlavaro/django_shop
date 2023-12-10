from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView

from main_app.models import Product, Category

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
    {'title': 'Создать', 'url_name': 'create_candle'},
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

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class CandlesListView(ListView):
    model = Product
    template_name = 'main_app/candles.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category=category, is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context

class CandleDetailView(DetailView):
    model = Product
    template_name = 'main_app/candle.html'
    context_object_name = 'object'

    def get_object(self, **kwargs):
        slug = self.kwargs['product_slug']
        product = get_object_or_404(Product, slug=slug)
        product.view_count += 1
        product.save()
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(category=context['object'].category)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['cat_selected'] = self.object.category_id
        return context

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

class CandleCreateView(CreateView):
    model = Product
    template_name = 'main_app/create_candle.html'
    fields = ['name', 'descriptions', 'photo', 'category', 'price', 'is_active', 'slug']
    success_url = reverse_lazy('main_app:index')
