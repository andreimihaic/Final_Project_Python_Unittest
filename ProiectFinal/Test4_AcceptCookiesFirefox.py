import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AcceptCookiesFirefox\
            (unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_accept_cookies(self):
        banner_cookies = self.driver.find_element(By.ID, "cookiebanner")
        time.sleep(1)

        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        time.sleep(1)

        self.assertTrue(banner_cookies.is_enabled(), "Banner-ul de cookies nu este afișat după acceptare.")

    def tearDown(self):
        self.driver.quit()