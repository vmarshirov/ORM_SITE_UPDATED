from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели Item в административном интерфейсе.

    Атрибуты:
        list_display    — поля, видимые в списке записей
        list_editable   — поля, редактируемые прямо в списке (без входа в запись)
        search_fields   — поля, по которым работает строка поиска
        list_filter     — поля для фильтрации в правой панели
        list_per_page   — количество записей на странице
        readonly_fields — поля, доступные только для чтения
        ordering        — порядок сортировки по умолчанию в admin
    """

    # Столбцы, отображаемые в списке записей
    list_display = ["id", "item_title", "item_nav", "item_nav_position", "item_content", "item_current_date"]

    # Поля, которые можно редактировать прямо из списка записей
    list_editable = ["item_title", "item_nav", "item_nav_position", "item_content"]

    # Строка поиска: ищет совпадения в указанных полях
    search_fields = ["item_title", "item_content"]

    # Фильтры в правой боковой панели
    list_filter = ["item_title", "item_current_date"]

    # Количество записей на одной странице списка
    list_per_page = 20

    # Поля только для чтения (не редактируются через admin)
    # current_date имеет auto_now=True, Django запрещает его редактирование
    readonly_fields = ["id", "item_current_date"]

    # Порядок сортировки: новые записи первыми
    ordering = ["item_nav_position"]


    