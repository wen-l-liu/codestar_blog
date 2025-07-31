from django.apps import AppConfig


class AboutConfig(AppConfig):
    """About application configuration.
    This class is used to configure the about application within the Django
    project.
    It sets the default primary key field type and the name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
