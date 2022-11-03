from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
er = 'Congratulations! You have successfully registered!'


def complete_required_fields():
    browser.find_element(By.XPATH, '//label[contains(text(),"First name*")]/following::input[@required]').send_keys("Alex")
    browser.find_element(By.XPATH, '//label[contains(text(),"Last name*")]/following::input[@required]').send_keys("Test")
    browser.find_element(By.XPATH, '//label[contains(text(),"Email*")]/following::input[@required]').send_keys("Alex@dot.com")
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()


try:
    browser = webdriver.Chrome()
    browser.get(link)
    complete_required_fields()
    ar = browser.find_element(By.TAG_NAME, 'h1').text
    assert ar == er, "ne proshlo"

finally:
    time.sleep(8)
    browser.quit()
