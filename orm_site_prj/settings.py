"""
settings.py — настройки проекта orm_site_prj.

Этот файл содержит все параметры конфигурации Django-проекта:
базы данных, приложения, middleware, шаблоны, статические файлы и т.д.

Документация Django по настройкам:
    https://docs.djangoproject.com/en/5.2/topics/settings/

Полный список параметров:
    https://docs.djangoproject.com/en/5.2/ref/settings/

ВНИМАНИЕ: перед деплоем в production обязательно выполните чеклист:
    https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Пути
# ---------------------------------------------------------------------------

# BASE_DIR — корневая директория проекта (там, где лежит manage.py).
# Path(__file__) → .../orm_site_prj/settings.py
# .resolve()     → абсолютный путь без симлинков
# .parent        → .../orm_site_prj/
# .parent        → .../  (корень проекта)
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Безопасность — ВАЖНО изменить перед production-деплоем
# ---------------------------------------------------------------------------

# SECRET_KEY используется для подписи сессий, CSRF-токенов и т.д.
# В production храните в переменной окружения: os.environ["DJANGO_SECRET_KEY"]
SECRET_KEY = "django-insecure-)y^0j8%!22a5_ldr#5)*cffjst3+*d&bv82%oq78lf$qm^@y^#"  # noqa: S105

# В production установите DEBUG = False и не используйте '*' в ALLOWED_HOSTS
DEBUG = True

# Список разрешённых хостов. '*' — принимать запросы с любого хоста (только для разработки).
ALLOWED_HOSTS = ["*"]


# ---------------------------------------------------------------------------
# Приложения проекта
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    # Стандартные приложения Django
    "django.contrib.admin",           # Административная панель
    "django.contrib.auth",            # Аутентификация пользователей
    "django.contrib.contenttypes",    # Фреймворк типов контента
    "django.contrib.sessions",        # Управление сессиями
    "django.contrib.messages",        # Flash-сообщения
    "django.contrib.staticfiles",     # Раздача статических файлов

    # Наше приложение сайта
    "site_app.apps.SiteAppConfig",
]


# ---------------------------------------------------------------------------
# Middleware — промежуточное ПО (обрабатывает запросы/ответы по цепочке)
# ---------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",            # Заголовки безопасности (HTTPS, HSTS)
    "django.contrib.sessions.middleware.SessionMiddleware",    # Управление сессиями
    "django.middleware.common.CommonMiddleware",               # Общие преобразования URL (слеш и т.д.)
    "django.middleware.csrf.CsrfViewMiddleware",               # Защита от CSRF-атак
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Связывает пользователя с запросом
    "django.contrib.messages.middleware.MessageMiddleware",    # Flash-сообщения через запросы
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Защита от кликджекинга (X-Frame-Options)
]


# ---------------------------------------------------------------------------
# URL-маршрутизация
# ---------------------------------------------------------------------------

# Модуль верхнего уровня, в котором Django ищет urlpatterns
ROOT_URLCONF = "orm_site_prj.urls"


# ---------------------------------------------------------------------------
# Шаблоны (Templates)
# ---------------------------------------------------------------------------

TEMPLATES = [
    {
        # Используем встроенный движок шаблонов Django
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Дополнительные директории для поиска шаблонов (кроме app/templates/)
        "DIRS": [BASE_DIR / "templates"],

        # APP_DIRS=True — Django ищет шаблоны в <app>/templates/ каждого приложения
        "APP_DIRS": True,

        "OPTIONS": {
            # Контекстные процессоры добавляют переменные в каждый шаблон автоматически
            "context_processors": [
                "django.template.context_processors.debug",    # Переменная debug в шаблоне
                "django.template.context_processors.request",  # Объект request в шаблоне
                "django.contrib.auth.context_processors.auth", # user, perms в шаблоне
                "django.contrib.messages.context_processors.messages",  # messages в шаблоне
            ],
        },
    },
]


# ---------------------------------------------------------------------------
# WSGI / ASGI — интерфейс веб-сервера
# ---------------------------------------------------------------------------

# Путь к WSGI-приложению (для запуска через gunicorn, uWSGI и т.д.)
WSGI_APPLICATION = "orm_site_prj.wsgi.application"


# ---------------------------------------------------------------------------
# База данных
# ---------------------------------------------------------------------------
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        # SQLite — файловая БД, идеальна для разработки и учебных проектов.
        # Для production используйте PostgreSQL: django.db.backends.postgresql
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------------------------
# Валидация паролей
# ---------------------------------------------------------------------------
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        # Пароль не должен быть похож на имя пользователя / email
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        # Минимальная длина пароля (по умолчанию 8 символов)
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        # Пароль не должен быть в списке распространённых паролей
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Пароль не должен состоять только из цифр
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ---------------------------------------------------------------------------
# Интернационализация (i18n / l10n)
# ---------------------------------------------------------------------------
# Документация: https://docs.djangoproject.com/en/5.2/topics/i18n/

# Язык интерфейса (используется в admin и стандартных сообщениях Django)
LANGUAGE_CODE = "ru-ru"

# Временная зона по умолчанию
TIME_ZONE = "Europe/Moscow"

# USE_I18N=True — включает переводы строк Django
USE_I18N = True

# USE_TZ=True — все datetime хранятся в UTC, конвертация в TIME_ZONE при отображении
USE_TZ = True


# ---------------------------------------------------------------------------
# Статические файлы (CSS, JavaScript, изображения)
# ---------------------------------------------------------------------------
# Документация: https://docs.djangoproject.com/en/5.2/howto/static-files/

# URL-префикс для статических файлов в браузере
STATIC_URL = "static/"

# В production: папка для collectstatic
# STATIC_ROOT = BASE_DIR / "staticfiles"


# ---------------------------------------------------------------------------
# Тип первичного ключа по умолчанию
# ---------------------------------------------------------------------------
# Документация: https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# BigAutoField — 64-битный автоинкремент (безопаснее, чем 32-битный AutoField)
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
