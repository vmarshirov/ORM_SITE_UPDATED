

```bash
# 1. Клонировать репозиторий
git clone <repo-url>
cd ....

# 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции (создаст db.sqlite3)
python manage.py makemigrations
python manage.py migrate

# 5. Создать суперпользователя для /admin/
python manage.py createsuperuser

# 6. Запустить сервер разработки
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000/

## Структура проекта

```
orm_site_prj/          ← корневая директория
├── manage.py          ← утилита управления Django
├── requirements.txt   ← зависимости Python
├── db.sqlite3         ← файл базы данных (создаётся после migrate)
│
├── orm_site_prj/      ← пакет настроек проекта
│   ├── settings.py    ← конфигурация проекта
│   ├── urls.py        ← корневой маршрутизатор URL
│   ├── wsgi.py        ← точка входа WSGI (production)
│   └── asgi.py        ← точка входа ASGI (async)
│
└── site_app/          ← основное приложение сайта
    ├── models.py      ← модель Item (таблица в БД)
    ├── views.py       ← обработчики HTTP-запросов
    ├── urls.py        ← маршруты приложения
    ├── admin.py       ← настройка Django Admin
    ├── apps.py        ← конфигурация приложения
    ├── tests.py       ← автоматические тесты
    ├── static/
    │   ├── css/mycss.css
    │   └── images/settings_django.png
    └── templates/
        ├── layout.html      ← базовый шаблон
        ├── index.html       ← главная страница
        ├── page.html        ← страница контента
        └── draft_page.html  ← статичный черновик
```

## URL-маршруты

| URL | View | Описание |
|-----|------|----------|
| `/` | `first_page` | Главная страница с инструкцией |
| `/page/<pk>` | `page` | Страница контента с pk из БД |
| `/admin/` | Django Admin | Управление записями |

## Модель Item

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | BigAutoField | Первичный ключ (авто) |
| `item_title` | CharField | Заголовок страницы |
| `item_nav` | CharField | Текст ссылки в навигации |
| `item_nav_position` | IntegerField | Позиция в меню (0 = скрыть) |
| `item_content` | TextField | HTML-содержимое страницы |
| `item_current_date` | DateTimeField | Дата изменения (авто) |

## Запуск тестов

```bash
python manage.py test site_app --verbosity=2
```

## ORM — полезные команды (Django shell)

```python
python manage.py shell

from site_app.models import Item

# Создать запись
new_item = Item.objects.create(
    item_title="Моя страница",
    item_nav="Ссылка",
    item_nav_position=10,
    item_content="<p>Содержимое</p>"
)

# Получить все записи
Item.objects.all()

# Фильтрация
Item.objects.filter(item_nav_position__gt=2)

# Получить одну запись
Item.objects.get(pk=1)

# Удалить все
Item.objects.all().delete()
```
