from django.shortcuts import render, get_object_or_404
from main_app.models import Product, Category
from django.views.generic import ListView, DetailView


class MainListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Главная страница'
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
        return context


class InfoListView(ListView):
    model = Product
    template_name = 'main_app/info.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Почему восковая свеча, а не парафиновая?'
        return context


class AboutListView(ListView):
    model = Product
    template_name = 'main_app/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Мастерская "Восковая свеча"'
        return context


class DeliveryListView(ListView):
    model = Product
    template_name = 'main_app/delivery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        context['title'] = 'Оплата и доставка'
        return context
