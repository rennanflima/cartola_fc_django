from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cartola_fc.core'

    def ready(self) -> None:
        import cartola_fc.core.receivers
