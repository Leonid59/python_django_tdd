from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начяать список и получить его позже"""
        # Домашняя страница приложения со списком дел
        self.browser.get('http://localhost:8000')

        # Заголовок и шапка страницы говорят о списе неотложных дел
        self.assertIn('To-Do' in self.browser.title)
        self.fail('Закончить тест')

        # Сразу предлагается ввести элемент чписка

        # Набираем в текстовом поле "Купить паввлиньи перья"

        # Когда нажимаем enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья"

        # Текстовое поле по-прежнемк предлагает добавить еще один элемент
        # Вводим "Сделать мушку из павлиньих перьев"

        # Страница снова обновляется

        # Видим, что сайт сгенерировал уникальный URL-адрес - об эжтом
        # выаодится сообщениее

        # Посетим этот URL-адрес - список по прежнему там


if __name__ == '__main__':
    unittest.main(warnings='ignore')
