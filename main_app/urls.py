from django.urls import path

from main_app.apps import MainAppConfig
from main_app.views import MainListView, InfoListView, AboutListView, DeliveryListView, ReviewsListView, \
    CandleDetailView, CandlesListView, CandleCreateView, CandleUpdateView

app_name = MainAppConfig.name

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('info/', InfoListView.as_view(), name='info'),
    path('about/', AboutListView.as_view(), name='about'),
    path('delivery/', DeliveryListView.as_view(), name='delivery'),
    path('reviews/', ReviewsListView.as_view(), name='reviews'),
    path('candles/<slug:category_slug>/', CandlesListView.as_view(), name='candles'),
    path('candle/<slug:product_slug>/', CandleDetailView.as_view(), name='candle'),
    path('create/', CandleCreateView.as_view(), name='create_candle'),
    path('update/<slug:slug>/', CandleUpdateView.as_view(), name='update_candle'),
]
