import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import soft_assertions, assert_that


class EnterAccount(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def test_enter_acount(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()

        account_button = self.driver.find_element(By.CSS_SELECTOR, ".ds-icon.outline-account.ds-icon-size__m").click()

        input_data = ['email_incorect@gmail.com','parola_incorecta']

        email_input = self.driver.find_element(By.ID, 'login[username]_id').send_keys(input_data[0])

        password_input = self.driver.find_element(By.ID, 'login[password]_id').send_keys(input_data[1])


        enter_account_button = self.driver.find_element(By.XPATH, "//button[@data-selen='login-submit']").click()

        invalid_message = self.driver.find_element(By.CSS_SELECTOR, ".sc-iGculD.bqfnYD")
        with soft_assertions():
            assert_that(invalid_message.text).ends_with('nevalidă.')

    def tearDown(self):
        self.driver.quit()
