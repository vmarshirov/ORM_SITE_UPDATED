"""
apps.py — конфигурация приложения site_app.

Класс AppConfig описывает метаданные Django-приложения и позволяет
выполнять инициализацию при запуске проекта (например, подключать сигналы).

Django автоматически обнаруживает этот класс, если в INSTALLED_APPS указан
путь "site_app.apps.SiteAppConfig" (или просто "site_app" для Django 3.2+).

Документация: https://docs.djangoproject.com/en/5.2/ref/applications/
"""

from django.apps import AppConfig


class SiteAppConfig(AppConfig):
    """
    Конфигурация приложения site_app.

    Attributes:
        default_auto_field: Тип поля первичного ключа по умолчанию
                            для всех моделей этого приложения.
                            BigAutoField — 64-битный автоинкремент (INT8).
        name:               Полный Python-путь к приложению
                            (совпадает с именем директории).
        verbose_name:       Человекочитаемое название приложения
                            (отображается в Django Admin).
    """

    # BigAutoField создаёт столбец BIGINT (8 байт) вместо INT (4 байта),
    # что позволяет хранить до 9.2 × 10^18 записей без переполнения.
    default_auto_field = "django.db.models.BigAutoField"

    # Имя Python-модуля приложения (директория с __init__.py)
    name = "site_app"

    # Название, отображаемое в заголовке раздела Django Admin
    verbose_name = "Приложение SITE_APP"
