import unittest
from app import app


class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        """Ініціалізація тестового середовища та HTTP-клієнта."""
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_product_found(self):
        """Тест сторінки для існуючого товару."""
        resp = self.client.get("/product/apple")
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("Назва продукту", html)
        self.assertIn("Apple", html)
        self.assertIn("35", html)
        self.assertIn("грн", html)

    def test_product_case_insensitive(self):
        """Запит на товар у довільному регістрі має працювати коректно."""
        resp = self.client.get("/product/mIlK")
        body = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        # Перевіряємо, що відображається нормалізована назва
        self.assertIn("Milk", body)
        self.assertIn("55", body)

    def test_product_missing(self):
        """Перевіряємо відповідь, коли товару не існує в каталозі."""
        resp = self.client.get("/product/chocolate")
        text = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("не знайдено", text)
        self.assertIn("chocolate", text)


if __name__ == "__main__":
    unittest.main()
