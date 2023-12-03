from django.urls import path

from main_app.apps import MainAppConfig
from main_app.views import candles, candle, MainListView, InfoListView, AboutListView, DeliveryListView, ReviewsListView

app_name = MainAppConfig.name

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('info/', InfoListView.as_view(), name='info'),
    path('about/', AboutListView.as_view(), name='about'),
    path('delivery/', DeliveryListView.as_view(), name='delivery'),
    path('reviews/', ReviewsListView.as_view(), name='reviews'),
    path('candles/<int:pk>/', candles, name='candles'),
    path('candle/<int:pk>/', candle, name='candle'),

]