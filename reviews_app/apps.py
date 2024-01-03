from django.apps import AppConfig


class ReviewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews_app'


    # Привязываем сигналы к приложению
    def ready(self):
        import reviews_app.signals
