from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main_app.models import Category
from reviews_app.models import Reviews


class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ['title', 'slug', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('reviews_app:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context


class ReviewsUpdateView(UpdateView):
    model = Reviews
    fields = ['title', 'slug', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('reviews_app:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context



class ReviewsListView(ListView):
    model = Reviews

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context

class ReviewsDetailView(DetailView):
    model = Reviews
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context

class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = reverse_lazy('reviews_app:list')

