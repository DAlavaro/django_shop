from django.shortcuts import render, get_object_or_404
from main_app.models import Product, Category
from django.views.generic import ListView, DetailView

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
]


class MainListView(ListView):
    model = Product

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

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'], is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = Category.objects.get(id=self.kwargs['pk'])
        context['menu'] = menu
        return context


class CandleDetailView(DetailView):
    model = Product

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        product.view_count += 1
        product.save()
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
        context['menu'] = menu
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


# class ReviewsListView(ListView):
#     model = Product
#     template_name = 'main_app/reviews.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu_catalog'] = Category.objects.all()
#         context['title'] = 'Отзывы'
#         context['menu'] = menu
#         return context