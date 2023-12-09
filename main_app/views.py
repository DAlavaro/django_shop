from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

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

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


# class CandlesListView(ListView):
#     model = Product
#     template_name = 'main_app/candles.html'
#     context_object_name = 'object_list'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu_catalog'] = Category.objects.filter(is_active=True)
#         context['title'] = 'Главная страница'
#         context['menu'] = menu
#         return context
#
#     def get_queryset(self):
#         slug = self.kwargs.get('slug')
#         queryset = super().get_queryset()
#         if slug:
#             queryset = queryset.filter(category__slug=slug, is_active=True)
#         return queryset


def candles(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = {
        'object_list': Product.objects.filter(category=category),
        'menu_catalog': Category.objects.all(),
        'title': category.name,
        'menu': menu,
    }
    return render(request, 'main_app/candles.html', context=context)


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


# def candle(request, product_slug):
#     product = get_object_or_404(Product, slug=product_slug)
#     context = {
#         'object': product,
#         'object_list': Product.objects.filter(product=product),
#         'menu_catalog': Category.objects.all(),
#         'title': product.name,
#         'menu': menu,
#         'cat_selected': product.category_id,
#     }
#     return render(request, 'main_app/candle.html', context=context)


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
