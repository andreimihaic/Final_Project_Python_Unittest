import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSocialMediaIcons(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()

    def test_share_buttons(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()

        social_media_icons = self.driver.find_elements(By.XPATH, "//ul[@class='Desktop-module__social-icons_pJ8mSq0870']/li")
        for icon in social_media_icons:
            self.assertTrue(icon.is_displayed(), f"Pictograma rețelelor sociale {icon.text} nu este afișat.")

    def tearDown(self):
        self.driver.quit()
