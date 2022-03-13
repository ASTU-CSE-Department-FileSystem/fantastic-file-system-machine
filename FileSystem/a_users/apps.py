from django.apps import AppConfig


class AUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_users'

    def ready(self):
        from .signals import max_number_of_users_type