"""
urls.py — корневой URL-конфигуратор проекта orm_site_prj.

Django ищет список urlpatterns в модуле, указанном в ROOT_URLCONF (settings.py).
Каждая запись в urlpatterns сопоставляет URL-шаблон с обработчиком (view).

Документация: https://docs.djangoproject.com/en/5.2/topics/http/urls/

Примеры:
    Функциональное представление:
        from myapp import views
        path("", views.home, name="home"),

    Классовое представление:
        from other_app.views import Home
        path("", Home.as_view(), name="home"),

    Включение дочернего маршрутизатора:
        from django.urls import include, path
        path("blog/", include("blog.urls")),
"""

from django.contrib import admin
from django.urls import include, path

# ---------------------------------------------------------------------------
# Список URL-маршрутов проекта верхнего уровня
# ---------------------------------------------------------------------------
urlpatterns = [
    # Маршрут к административной панели Django (/admin/)
    # admin.site.urls — встроенный маршрутизатор Django Admin
    path("admin/", admin.site.urls),

    # Все остальные URL делегируются в маршрутизатор приложения site_app.
    # include() подключает site_app/urls.py и «монтирует» его на корень "/"
    path("", include("site_app.urls")),
]
