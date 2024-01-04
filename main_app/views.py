from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from main_app.models import Product, Category
from django.views.generic import ListView, DetailView
=======
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main_app.models import Product, Category

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
    {'title': 'Создать', 'url_name': 'create_candle'},
]
>>>>>>> main


class MainListView(ListView):
    model = Product
<<<<<<< HEAD
=======
    template_name = 'main_app/index.html'
    context_object_name = 'object_list'
>>>>>>> main

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
<<<<<<< HEAD
=======
        context['menu'] = menu
>>>>>>> main
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class CandlesListView(ListView):
    model = Product
    template_name = 'main_app/candles.html'
<<<<<<< HEAD

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'], is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = Category.objects.get(id=self.kwargs['pk'])
        return context


class CandleDetailView(DetailView):
    model = Product

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
=======
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
>>>>>>> main
        product.view_count += 1
        product.save()
        return product

<<<<<<< HEAD
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        return context


=======
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Product.objects.filter(category=context['object'].category)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['cat_selected'] = self.object.category_id
        return context

>>>>>>> main
class InfoListView(ListView):
    model = Product
    template_name = 'main_app/info.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Почему восковая свеча, а не парафиновая?'
<<<<<<< HEAD
=======
        context['menu'] = menu
>>>>>>> main
        return context


class AboutListView(ListView):
    model = Product
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Мастерская "Восковая свеча"'
<<<<<<< HEAD
=======
        context['menu'] = menu
>>>>>>> main
        return context


class DeliveryListView(ListView):
    model = Product
    template_name = 'main_app/delivery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Оплата и доставка'
<<<<<<< HEAD
=======
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
    template_name = 'main_app/crud/create_candle.html'
    fields = ['name', 'descriptions', 'photo', 'category', 'price', 'is_active', 'slug']
    success_url = reverse_lazy('main_app:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Добавление товара'
        context['menu'] = menu
        return context

class CandleUpdateView(UpdateView):
    model = Product
    template_name = 'main_app/crud/create_candle.html'
    fields = ['name', 'descriptions', 'photo', 'category', 'price', 'is_active', 'slug']

    def get_success_url(self, **kwargs):
        return reverse('main_app:candle', args=(self.object.slug,))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Добавление товара'
        context['menu'] = menu
        return context


class CandleDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main_app:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Добавление товара'
        context['menu'] = menu
>>>>>>> main
        return context
