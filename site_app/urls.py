"""
urls.py — URL-конфигурация приложения site_app.

Этот файл подключается в корневом orm_site_prj/urls.py через:
    path("", include("site_app.urls"))

app_name задаёт пространство имён (namespace) для именованных URL,
что позволяет использовать {% url 'site_app:page' pk=1 %} в шаблонах
и reverse('site_app:page', kwargs={'pk': 1}) в Python-коде.

Документация: https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.urls import path

from . import views

# Пространство имён приложения.
# Используется при именовании URL: {% url 'site_app:page' pk=1 %}
app_name = "site_app"

urlpatterns = [
    # Корневой URL "/" — главная страница.
    # name="index" позволяет ссылаться на неё через {% url 'site_app:index' %}
    path("", views.first_page, name="index"),

    # URL вида "/page/1", "/page/42" и т.д.
    # <int:pk> — конвертер типов: захватывает целое число и передаёт в view как pk.
    # Если pk не целое число — Django автоматически вернёт 404.
    path("page/<int:pk>", views.page, name="page"),
]
