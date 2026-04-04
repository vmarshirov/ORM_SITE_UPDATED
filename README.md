

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


## ORM — полезные команды (Django shell)

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

# Удалить
Item.objects.all().filter(id__gte=2).delete()
Item.objects.all().delete()