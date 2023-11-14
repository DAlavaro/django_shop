from django.urls import path

from main_app.views import index, about

urlpatterns = [
    path('', index),
    path('about/', about),
]