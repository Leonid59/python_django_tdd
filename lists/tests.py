from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):
    """тест добашней страницы"""

    def test_uses_home_template(self):
        """тест: домашняя страница возвращает правильный html"""
        responce = self.client.get('/')
        self.assertTemplateUsed(responce, 'home.html')

    def test_can_save_a_POST_request(self):
        """тест: сохранить post-запрос"""
        responce = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', responce.content.decode())
        self.assertTemplateUsed(responce, 'home.html')