import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait



@pytest.mark.usefixtures('browser')
class TestHomepage:

    def test_homepage(self, browser):
        browser.get('https://uchi.ru/')
        #element1 = driver.find_element(By.CSS_SELECTOR, '#id_login')

        #wait = WebDriverWait(driver, 5)
        #element = wait.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#id_login'))

