import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchProducts(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    HANDLE_BUTTON = (By.XPATH, '//a[text()="Du-te la magazin"]')
    BUTTON_SEARCH = (By.ID, "algoliaButton")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_products(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.HANDLE_BUTTON).click()
        self.driver.find_element(*self.BUTTON_SEARCH).click()

        query_button = (self.driver.find_element(By.CLASS_NAME, "ds-input-field-input"))
        query_button.send_keys("telefon")
        query_button.send_keys(Keys.ENTER)

        products = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "ds-product-tile__m")))

        results = {}
        for i, product in enumerate(products):
            results[f"Produs {i + 1}"] = product.text

        for key, value in results.items():
            print(f'{key}: {value}')

        self.assertGreaterEqual(len(results), 1, "Nu s-a gasit niciun rezultat.")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()