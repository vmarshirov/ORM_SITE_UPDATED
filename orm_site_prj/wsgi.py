"""
wsgi.py — WSGI-конфигурация проекта orm_site_prj.

WSGI (Web Server Gateway Interface) — стандартный интерфейс между
веб-сервером (nginx, Apache) и Python-приложением.

Этот модуль экспортирует переменную ``application``, которую используют
WSGI-совместимые серверы (gunicorn, uWSGI):

    gunicorn orm_site_prj.wsgi:application

Документация: https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Указываем Django, какой модуль настроек использовать.
# setdefault() не перезапишет значение, если переменная уже задана в окружении,
# что позволяет переопределять настройки через ENV без изменения кода.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_site_prj.settings")

# Создаём WSGI-приложение на основе текущих настроек.
# gunicorn/uWSGI вызывают этот объект при каждом HTTP-запросе.
application = get_wsgi_application()
