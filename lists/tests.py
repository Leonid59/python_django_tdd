from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    """тест добашней страницы"""

    def test_uses_home_template(self):
        """тест: домашняя страница возвращает правильный html"""
        responce = self.client.get('/')
        self.assertTemplateUsed(responce, 'home.html')
