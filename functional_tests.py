from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        """тест: можно начать список и получить его позже"""
        # Домашняя страница приложения со списком дел
        self.browser.get('http://localhost:8000')

        # Заголовок и шапка страницы говорят о списе неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Сразу предлагается ввести элемент чписка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Набираем в текстовом поле "Купить паввлиньи перья"
        inputbox.send_keys('Купить павлиньи перья')

        # Когда нажимаем enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])

        # Текстовое поле по-прежнемк предлагает добавить еще один элемент
        # Вводим "Сделать мушку из павлиньих перьев"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Страница снова обновляется
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Купить павлиньи перья', [row.text for row in rows])
        self.assertIn('2: Сделать мушку из павлиньих перьев', [row.text for row in rows])

        # Видим, что сайт сгенерировал уникальный URL-адрес - об этом
        # выводится сообщениее
        self.fail('Закаончить тест!')
        
        # Посетим этот URL-адрес - список по прежнему там


if __name__ == '__main__':
    unittest.main(warnings='ignore')
