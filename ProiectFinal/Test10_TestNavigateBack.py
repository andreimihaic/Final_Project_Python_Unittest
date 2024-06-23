import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestNavigateBack(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    BUTTON_SEARCH = (By.ID, "algoliaButton")
    INITIAL_URL = "https://www.sinsay.com/ro/ro/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.INITIAL_URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACCEPT_COOKIES)).click()

    def search_for_product(self, query):
        self.driver.find_element(*self.BUTTON_SEARCH).click()
        query_button = self.driver.find_element(By.CLASS_NAME, "ds-input-field-input")
        query_button.send_keys(query)
        query_button.send_keys(Keys.ENTER)

    def click_fifth_product(self):
        list_products = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                                                    ".ds-product-tile.ds-product-tile__m.AlgoliaProducts-module__algolia-products-product-tile")))
        fifth_product = list_products[4]
        fifth_product.click()

    def test_navigate_back(self):
        self.search_for_product("pantofi")
        self.click_fifth_product()

        while self.driver.current_url != self.INITIAL_URL:
            self.driver.back()

        self.assertEqual(self.INITIAL_URL, self.driver.current_url, "URL-ul inițial nu este același cu URL-ul curent.")

    def tearDown(self):
        self.driver.quit()
