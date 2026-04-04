"""
views.py — представления (views) приложения site_app.

View (представление) — функция или класс, которая принимает HTTP-запрос
(HttpRequest) и возвращает HTTP-ответ (HttpResponse).

Поток обработки запроса:
    Браузер → urls.py → view-функция → шаблон → HttpResponse → Браузер

Документация: https://docs.djangoproject.com/en/5.2/topics/http/views/
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Item


def first_page(request: HttpRequest) -> HttpResponse:
    """
    Главная страница сайта (/).

    Отображает стартовую страницу с инструкцией по работе с проектом.
    Не требует данных из БД — шаблон статический.

    Args:
        request: объект HTTP-запроса от Django.

    Returns:
        HttpResponse с отрендеренным шаблоном index.html.
    """
    return render(request, "index.html")


def page(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Страница содержимого по первичному ключу (/page/<pk>).

    Загружает из БД:
    - nav_objects  — список всех страниц с ненулевой позицией в навигации
                     (для построения меню вкладок).
    - content_object — конкретная запись с переданным pk
                       (содержимое текущей страницы).

    Args:
        request: объект HTTP-запроса от Django.
        pk:      первичный ключ (id) записи Item в базе данных.

    Returns:
        HttpResponse с отрендеренным шаблоном page.html.

    Raises:
        Http404: если запись с переданным pk не найдена в БД.
                 (get_object_or_404 вместо .get() — безопасно возвращает 404)
    """
    # Получаем только нужные поля для навигации, отфильтровав скрытые записи
    # (item_nav_position=0 означает «не показывать в меню»).
    # .values() возвращает QuerySet словарей, что экономит память.
    nav_objects = (
        Item.objects
        .values("id", "item_nav", "item_nav_position")
        .filter(item_nav_position__gt=0)
        .order_by("-item_nav_position")
    )

       
    content_object = Item.objects.get(pk=pk)

    # Контекст — словарь переменных, передаваемых в шаблон.
    # В шаблоне доступны как {{ pk }}, {{ nav_objects }}, {{ content_object }}
    context = {
        "pk": pk,
        "nav_objects": nav_objects,
        "content_object": content_object,
    }

    return render(request, "page.html", context)
