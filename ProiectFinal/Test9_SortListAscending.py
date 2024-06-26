import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSortListAscending(unittest.TestCase):
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

        query_button = self.driver.find_element(By.CLASS_NAME, "ds-input-field-input")
        query_button.send_keys("caiet")
        query_button.send_keys(Keys.ENTER)

        all_list = self.driver.find_elements(By.CSS_SELECTOR,
                                             '.ds-product-tile.ds-product-tile__m.AlgoliaProducts-module__algolia-products-product-tile')

        sorted_product_list = sorted(all_list, key=lambda x: float(
            x.find_element(By.CLASS_NAME, "ds-text-size__xl").text.replace("RON", "").replace(",", ".")))

        name_products = self.driver.find_elements(By.CLASS_NAME, 'ds-product-tile-name')

        for i, (product, price) in enumerate(zip(name_products, sorted_product_list), start=1):
            price_value = price.find_element(By.CLASS_NAME, "ds-text-size__xl").text
            print(f'Produs {i}: {price_value}')

        sorted_product_list = sorted(all_list, key=lambda x: float(
            x.find_element(By.CLASS_NAME, "ds-text-size__xl").text.replace("RON", "").replace(",", ".")))

        for i in range(len(sorted_product_list) - 1):
            current_price = float(
                sorted_product_list[i].find_element(By.CLASS_NAME, "ds-text-size__xl").text.replace("RON", "").replace(
                    ",", "."))
            next_price = float(
                sorted_product_list[i + 1].find_element(By.CLASS_NAME, "ds-text-size__xl").text.replace("RON",
                                                                                                        "").replace(",",
                                                                                                                    "."))
            assert current_price <= next_price, "Produsele nu sunt sortate crescător!"


def tearDown(self):
    self.driver.quit()
