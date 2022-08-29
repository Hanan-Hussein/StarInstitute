from django.apps import AppConfig


class StarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'star'

    def ready(self):
        import star.signals