from assertpy import soft_assertions, assert_that
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestChangeLanguage(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/ro/ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def test_change_language(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_COOKIES)).click()
        
        language_selector = self.driver.find_element(By.XPATH,"//div[contains(@class,'StoreSelector-module__wrapper')]")
        language_selector.click()

        language_option = self.driver.find_element(By.CLASS_NAME,'outline-chevron-down')
        language_option.click()

        select_language = self.driver.find_element(By.XPATH,"//span[contains(text(),'Global store')]")
        select_language.click()

        go_to_store = self.driver.find_element(By.CLASS_NAME,'sc-fWSDcn')
        go_to_store.click()

        with soft_assertions():
            assert_that(self.driver.current_url).contains('en')

    def tearDown(self):
        self.driver.quit()
        