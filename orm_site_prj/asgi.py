"""
asgi.py — ASGI-конфигурация проекта orm_site_prj.

ASGI (Asynchronous Server Gateway Interface) — современный стандарт интерфейса
между веб-сервером и Python-приложением, поддерживающий асинхронность
(WebSockets, HTTP/2, long-polling).

Этот модуль экспортирует переменную ``application``, которую используют
ASGI-совместимые серверы (Daphne, Uvicorn):

    uvicorn orm_site_prj.asgi:application

Документация: https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Указываем Django, какой модуль настроек использовать.
# При необходимости можно переопределить через ENV: DJANGO_SETTINGS_MODULE=...
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_site_prj.settings")

# Создаём ASGI-приложение. Для добавления WebSocket-поддержки здесь можно
# подключить django-channels:
#   from channels.routing import ProtocolTypeRouter
#   application = ProtocolTypeRouter({...})
application = get_asgi_application()
