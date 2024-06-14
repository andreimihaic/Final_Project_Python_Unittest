import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NavigateBack(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    BUTTON_SEARCH = (By.ID, "algoliaButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/ro/ro/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACCEPT_COOKIES)).click()

    def test_navigate_back(self):
        self.driver.find_element(*self.BUTTON_SEARCH).click()

        query_button = (self.driver.find_element(By.CLASS_NAME, "ds-input-field-input"))
        query_button.send_keys("pantofi")
        query_button.send_keys(Keys.ENTER)

        list_products = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                        ".ds-product-tile.ds-product-tile__m.AlgoliaProducts-module__algolia-products-product-tile")))
        fifth_product = list_products[4]
        fifth_product.click()

        while self.driver.current_url != 'https://www.sinsay.com/ro/ro/':
            self.driver.back()
        time.sleep(5)

        self.assertEqual("https://www.sinsay.com/ro/ro/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
