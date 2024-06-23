import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckSearchButtonIsDisplayed(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')
    BUTTON_SEARCH = (By.ID, "algoliaButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_button_is_displayed(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()

        search_button = self.driver.find_element(*self.BUTTON_SEARCH)
        assert search_button.is_displayed(), "Butonul de căutare nu este vizibil."

    def tearDown(self):
        self.driver.quit()
