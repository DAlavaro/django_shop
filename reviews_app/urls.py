from django.urls import path

from reviews_app.apps import ReviewsAppConfig
from reviews_app.views import ReviewsCreateView, ReviewsListView, ReviewsDetailView, ReviewsUpdateView, ReviewsDeleteView

app_name = ReviewsAppConfig.name

urlpatterns = [
    path('create/', ReviewsCreateView.as_view(), name="create"),
    path('', ReviewsListView.as_view(), name="list"),
    path('view/<slug:slug>/', ReviewsDetailView.as_view(), name="view"),
    path('edit/<slug:slug>/', ReviewsUpdateView.as_view(), name="edit"),
    path('delete/<slug:slug>/', ReviewsDeleteView.as_view(), name="delete"),
]