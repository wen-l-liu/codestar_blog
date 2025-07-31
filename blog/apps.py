from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Blog application configuration.
    This class is used to configure the blog application within the Django
    project.
    It sets the default primary key field type and the name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
