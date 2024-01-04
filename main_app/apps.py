from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    verbose_name = 'Восковые свечи'

# Привязываем сигналы к приложению
    def ready(self):
        import main_app.signals