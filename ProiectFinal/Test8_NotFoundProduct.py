import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestNotFoundProduct(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')
    BUTTON_SEARCH = (By.ID, "algoliaButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def test_not_found_product(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()
        self.driver.find_element(*self.BUTTON_SEARCH).click()

        query_button = (self.driver.find_element(By.CLASS_NAME, "ds-input-field-input"))
        query_button.send_keys("inexistent")
        query_button.send_keys(Keys.ENTER)

        try:
            error_message = self.driver.find_element(By.XPATH, "//span[contains(text(),'Nu s-au putut găsi produsele pentru fraza introdusă')]")
            self.assertTrue(error_message.is_displayed(),
                            "Mesajul de eroare 'Nu s-au putut găsi produsele...' nu este afișat.")
        except NoSuchElementException:
            self.fail('Produsul nu a fost gasit.')

    def tearDown(self):
        self.driver.quit()
