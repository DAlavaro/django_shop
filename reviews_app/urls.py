from django.urls import path

from reviews_app.apps import ReviewsAppConfig
from reviews_app.views import ReviewsCreateView, ReviewsListView

app_name = ReviewsAppConfig.name

urlpatterns = [
    path('create/', ReviewsCreateView.as_view(), name="create"),
    # path('', ReviewsListView.as_view(), name="list"),
    # path('view/<int:pk>/', ..., name="view"),
    # path('edit/<int:pk>/', ..., name="edit"),
    # path('delete/<int:pk>/', ..., name="delete"),
]