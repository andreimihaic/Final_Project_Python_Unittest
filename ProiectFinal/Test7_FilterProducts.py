import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestFilterProducts(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')
    BUTTON_SEARCH = (By.ID, "algoliaButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_filter_products(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()
        self.driver.find_element(*self.BUTTON_SEARCH).click()

        query_button = (self.driver.find_element(By.CLASS_NAME, "ds-input-field-input"))
        query_button.send_keys("tricouri")
        query_button.send_keys(Keys.ENTER)

        characteristics = self.driver.find_elements(By.CSS_SELECTOR,
                                                    ".ds-accordion.ds-accordion__inner-spacing.ds-accordion__size-s")

        categori = characteristics[0].click()
        select_gender = self.driver.find_elements(By.CLASS_NAME, "checkbox-container")
        man = select_gender[1].click()

        size = characteristics[1].click()
        l = self.driver.find_element(By.XPATH, "//span[text()='L']").click()

        colors = characteristics[2].click()
        white = self.driver.find_element(By.XPATH, "//div[contains(@class, 'Colors-module__colorVariant') and contains(@style, 'background: white')]").click()


        products_list = self.driver.find_elements(By.CLASS_NAME, "AlgoliaProducts-module__algolia-products-container")

        for products in products_list:
            assert 'Tricou' in products.text, "Produsul nu este un tricou."


    def tearDown(self):
        self.driver.quit()
