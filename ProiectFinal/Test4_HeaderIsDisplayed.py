import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHeaderIsDisplayed(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_header_is_displayed(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.HANDLE_BUTTON)).click()

        header = self.driver.find_element(By.CLASS_NAME, "Desktop-module__wrapper")
        self.assertTrue(header.is_displayed(), "Antetul nu este afișat")

    def tearDown(self):
        self.driver.quit()
