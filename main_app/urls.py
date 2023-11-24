from django.urls import path

from main_app.apps import MainAppConfig
from main_app.views import index, about, info, delivery, reviews

app_name = MainAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),

]