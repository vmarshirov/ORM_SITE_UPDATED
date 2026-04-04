#!/usr/bin/env python
"""
manage.py — стандартная утилита командной строки Django для административных задач.

Использование:
    python manage.py runserver          — запустить dev-сервер
    python manage.py makemigrations     — создать файлы миграций
    python manage.py migrate            — применить миграции к БД
    python manage.py createsuperuser    — создать суперпользователя
    python manage.py shell              — открыть Django shell
    python manage.py help               — список всех команд
"""

import os
import sys


def main():
    """Запустить административную задачу Django."""
    # Устанавливаем переменную окружения с путём к модулю настроек проекта.
    # Это позволяет Django найти файл settings.py при любом вызове manage.py.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_site_prj.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Django не установлен или не активирован virtualenv
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен "
            "и доступен через переменную PYTHONPATH. "
            "Возможно, не активирован виртуальный environment?"
        ) from exc

    # Передаём аргументы командной строки (sys.argv) в Django
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
