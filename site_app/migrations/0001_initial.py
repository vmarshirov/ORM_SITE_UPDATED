"""
0001_initial.py — первоначальная миграция: создание таблицы site_app_item.

Файлы миграций генерируются автоматически командой:
    python manage.py makemigrations

Применяются командой:
    python manage.py migrate

Документация: https://docs.djangoproject.com/en/5.2/topics/migrations/

НЕ РЕДАКТИРУЙТЕ этот файл вручную без крайней необходимости.
Для изменения схемы БД — изменяйте models.py и запускайте makemigrations.
"""

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    """Первоначальное создание таблицы для модели Item."""

    # initial=True — Django знает, что это первая миграция для приложения
    initial = True

    # dependencies — список миграций, которые должны быть применены до этой.
    # Для первой миграции зависимостей нет.
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                # Первичный ключ — 64-битный автоинкремент (BigAutoField)
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # Заголовок страницы
                (
                    "item_title",
                    models.CharField(
                        default="Заголовок",
                        max_length=255,
                        verbose_name="Заголовок (title)",
                        help_text="Отображается в теге <title> страницы и как заголовок контента.",
                    ),
                ),
                # Текст ссылки в навигации
                (
                    "item_nav",
                    models.CharField(
                        default="Название ссылки",
                        max_length=255,
                        verbose_name="Название ссылки",
                        help_text="Текст, отображаемый в навигационном меню.",
                    ),
                ),
                # Позиция в навигационном меню
                (
                    "item_nav_position",
                    models.IntegerField(
                        default=1,
                        verbose_name="Приоритет ссылки в навигации (0 — исключить)",
                        help_text="Чем больше число — тем правее ссылка. 0 — скрыть из навигации.",
                    ),
                ),
                # HTML-содержимое страницы
                (
                    "item_content",
                    models.TextField(
                        default=(
                            '<a id="top_of_page" href="#h1" class="card-link">На раздел 1</a>'
                            "&nbsp;&nbsp;"
                            '<h6 class="card-subtitle mb-2 text-body-secondary">'
                            '<a id="h1">Раздел 1</a></h6>'
                            '<p class="card-text">Содержание раздела 1</p>'
                            '<img src="/static/images/settings_django.png" height="30px">'
                            "&nbsp;&nbsp;"
                            '<a href="#top_of_page" class="card-link">к началу страницы</a>'
                        ),
                        verbose_name="Основное содержание страницы",
                        help_text="HTML-содержимое страницы. Отображается без экранирования.",
                    ),
                ),
                # Дата последнего изменения (обновляется автоматически)
                (
                    "item_current_date",
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name="Дата записи",
                        help_text="Обновляется автоматически при каждом сохранении объекта.",
                    ),
                ),
            ],
            options={
                # Человекочитаемые названия для Django Admin
                "verbose_name": "Содержание текущей страницы",
                "verbose_name_plural": "Содержание всех страниц",
                # Сортировка по умолчанию: убывание по позиции в навигации
                "ordering": ("-item_nav_position",),
            },
        ),
    ]
