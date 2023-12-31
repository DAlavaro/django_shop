from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from reviews_app.models import Reviews


class ReviewsCreateView(CreateView):
    model = Reviews
    fields = ['title', 'slug', 'content', 'photo', 'is_published']
    success_url = reverse_lazy('main_app:index')


class ReviewsListView(ListView):
    model = Reviews

