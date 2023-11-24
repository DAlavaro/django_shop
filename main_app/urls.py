from django.urls import path

from main_app.apps import MainAppConfig
from main_app.views import index, about

app_name = MainAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('info/', index, name='info'),
    path('about/', about, name='about'),
    path('delivery/', index, name='delivery'),
    path('reviews/', index, name='reviews'),

]