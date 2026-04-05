"""
models.py — модели данных приложения site_app.

Модель — это Python-класс, унаследованный от django.db.models.Model.
Каждый класс соответствует одной таблице в базе данных.
Каждый атрибут класса — столбцу таблицы.

После изменения моделей обязательно выполните:
    python manage.py makemigrations   # создать файл миграции
    python manage.py migrate          # применить миграцию к БД

Документация: https://docs.djangoproject.com/en/5.2/topics/db/models/
"""

from django.db import models
from django.urls import reverse


class Item(models.Model):
    """
    Модель одной страницы сайта.

    Хранит заголовок страницы, текст ссылки в навигации, приоритет
    отображения, HTML-содержимое и дату последнего изменения.

    Таблица в БД: site_app_item
    """

    # ------------------------------------------------------------------
    # Поля модели
    # ------------------------------------------------------------------

    item_title = models.CharField(
        verbose_name="title",
        max_length=255,
        default="Заголовок",
        help_text="Отображается в теге title страницы и как заголовок контента.",
    )
    
    item_nav = models.CharField(
        verbose_name="Ссылка",
        max_length=255,
        default="Название ссылки",
        help_text="Текст, отображаемый в навигационном меню.",
    )
  

    item_nav_position = models.IntegerField(
        verbose_name="НавигПриорит(0—Искл)",
        default=1,
        help_text="Чем больше число — тем правее ссылка. 0 — скрыть из навигации.",
    )

    item_content = models.TextField(
        verbose_name="Содержание страницы",
        default=(
            '<a id="top_of_page" href="#h1" class="card-link">На раздел 1</a>'
            '&nbsp;&nbsp;'
            '<h6 class="card-subtitle mb-2 text-body-secondary">'
            '<a id="h1">Раздел 1</a></h6>'
            '<p class="card-text">Содержание раздела 1</p>'
            '<img src="/static/images/settings_django.png" height="30px">'
            '<br>'
            '<a href="#top_of_page" class="card-link">к началу страницы</a>'
        ),
        help_text="HTML-содержимое страницы. Отображается без экранирования (autoescape off).",
    )
    """Тело страницы в формате HTML. Вставляется в шаблон через {% autoescape off %}."""

    item_current_date = models.DateTimeField(
        verbose_name="Дата записи",
        auto_now=True,
        help_text="Обновляется автоматически при каждом сохранении объекта.",
    )

    # ------------------------------------------------------------------
    # Метаданные модели
    # ------------------------------------------------------------------

    class Meta:
        """Мета-настройки модели Item."""

        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

        # Сортировка по умолчанию
        ordering = ("item_nav_position",)

    # ------------------------------------------------------------------
    # Строковое представление объекта
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """Возвращает человекочитаемое представление записи (для admin и shell)."""
        return f" item_nav_position: {self.item_nav_position}, pk: {self.pk};  item_title: {self.item_title}"

    # ------------------------------------------------------------------
    # URL объекта
    # ------------------------------------------------------------------

    def get_absolute_url(self) -> str:
        """
        Возвращает URL страницы, соответствующей этой записи.

        Используется в шаблонах: {{ object.get_absolute_url }}
        и в admin для кнопки «Смотреть на сайте».
        """
        return reverse("site_app:page", kwargs={"pk": self.pk})
