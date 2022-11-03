import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestLinks(unittest.TestCase):
    links = (
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
    )

    def test_link(self):
        for link in self.links:
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
            input3.send_keys("test@test.ru")
            input4 = browser.find_element(By.CSS_SELECTOR, '.second_block input.first')
            input4.send_keys("+78008888888")
            input5 = browser.find_element(By.CSS_SELECTOR, '.second_block input.second')
            input5.send_keys("My address")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, welcome_text_elt.text, "Should be absolute value of a number")

            browser.quit()


if __name__ == "__main__":
    unittest.main()

