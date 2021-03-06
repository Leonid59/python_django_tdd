from django.test import TestCase
from lists.models import Item

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
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertIn('A new list item', responce.content.decode())
        self.assertTemplateUsed(responce, 'home.html')

class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранение и получение элементов списка"""
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
