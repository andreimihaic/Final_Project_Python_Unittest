import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoTOStore(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_go_to_store(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.HANDLE_BUTTON)).click()

        new_url = self.driver.current_url
        expected_url = "https://www.sinsay.com/ro/ro/"

        self.assertEqual(new_url, expected_url, "URL-ul așteptat nu corespunde URL-ului actual: {new_url}")

    def tearDown(self):
        self.driver.quit()
