"""
tests.py — автоматические тесты приложения site_app.

Тесты проверяют корректность моделей, URL-маршрутов и представлений.
Запуск всех тестов: python manage.py test
Запуск тестов приложения: python manage.py test site_app
Запуск с отображением вывода: python manage.py test --verbosity=2

Документация: https://docs.djangoproject.com/en/5.2/topics/testing/
"""

from django.test import Client, TestCase
from django.urls import reverse

from .models import Item


class ItemModelTest(TestCase):
    """Тесты модели Item."""

    def setUp(self):
        """Создаём тестовую запись перед каждым тестом."""
        # setUp() вызывается перед каждым методом test_*
        # Все изменения в БД откатываются после каждого теста (транзакция).
        self.item = Item.objects.create(
            item_title="Тестовый заголовок",
            item_nav="Тестовая ссылка",
            item_nav_position=5,
            item_content="<p>Тестовое содержимое</p>",
        )

    def test_item_str(self):
        """__str__ должен возвращать строку с pk и item_title."""
        expected = f"pk: {self.item.pk};  item_title: Тестовый заголовок"
        self.assertEqual(str(self.item), expected)

    def test_item_get_absolute_url(self):
        """get_absolute_url() должен возвращать URL вида /page/<pk>."""
        url = self.item.get_absolute_url()
        self.assertEqual(url, f"/page/{self.item.pk}")

    def test_item_default_nav_position(self):
        """Значение по умолчанию item_nav_position должно быть 1."""
        item = Item.objects.create(item_title="Без позиции")
        self.assertEqual(item.item_nav_position, 1)

    def test_item_ordering(self):
        """
        Записи должны сортироваться по убыванию item_nav_position.
        Запись с большим приоритетом должна идти первой.
        """
        Item.objects.create(item_title="Низкий приоритет", item_nav_position=1)
        Item.objects.create(item_title="Высокий приоритет", item_nav_position=99)
        first = Item.objects.first()
        self.assertEqual(first.item_title, "Высокий приоритет")


class ItemViewTest(TestCase):
    """Тесты представлений (views) приложения."""

    def setUp(self):
        """Создаём тестового клиента и тестовую запись."""
        # Client — тестовый HTTP-клиент Django, имитирует браузер
        self.client = Client()
        self.item = Item.objects.create(
            item_title="Страница тест",
            item_nav="Ссылка тест",
            item_nav_position=1,
            item_content="<p>Контент</p>",
        )

    def test_index_page_status_code(self):
        """Главная страница (/) должна возвращать HTTP 200."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        """Главная страница должна использовать шаблон index.html."""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_page_view_status_code(self):
        """Страница /page/<pk> с существующим pk должна возвращать HTTP 200."""
        url = reverse("site_app:page", kwargs={"pk": self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_page_view_404(self):
        """Страница /page/<pk> с несуществующим pk должна возвращать HTTP 404."""
        url = reverse("site_app:page", kwargs={"pk": 99999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_page_view_context(self):
        """Контекст шаблона page.html должен содержать pk, nav_objects, content_object."""
        url = reverse("site_app:page", kwargs={"pk": self.item.pk})
        response = self.client.get(url)
        self.assertIn("pk", response.context)
        self.assertIn("nav_objects", response.context)
        self.assertIn("content_object", response.context)

    def test_page_view_uses_correct_template(self):
        """Страница /page/<pk> должна использовать шаблон page.html."""
        url = reverse("site_app:page", kwargs={"pk": self.item.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "page.html")

    def test_nav_excludes_zero_position(self):
        """
        Записи с item_nav_position=0 не должны попадать в навигацию.
        """
        # Создаём скрытую запись (position=0)
        hidden = Item.objects.create(
            item_title="Скрытая",
            item_nav="Скрытая ссылка",
            item_nav_position=0,
        )
        url = reverse("site_app:page", kwargs={"pk": self.item.pk})
        response = self.client.get(url)
        nav_ids = [obj["id"] for obj in response.context["nav_objects"]]
        self.assertNotIn(hidden.pk, nav_ids)
