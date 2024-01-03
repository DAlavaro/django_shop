from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from main_app.models import Category
from reviews_app.models import Reviews
from pytils.translit import slugify


class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ['title', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('reviews_app:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            return super().form_valid(form)


class ReviewsUpdateView(UpdateView):
    model = Reviews
    fields = ['title', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('reviews_app:list')

    def get_success_url(self):
        return reverse('reviews_app:view', kwargs={'slug': self.object.slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context


class ReviewsListView(ListView):
    model = Reviews

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context

class ReviewsDetailView(DetailView):
    model = Reviews

    def get_object(self, queryset=None):
        self.object = super().get_object(
            queryset=queryset
        )
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_catalog'] = Category.objects.all()
        return context

class ReviewsDeleteView(DeleteView):
    model = Reviews
    success_url = reverse_lazy('reviews_app:list')

