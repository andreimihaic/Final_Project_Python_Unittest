import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddProductCart(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")
    BUTTON_SEARCH = (By.ID, "algoliaButton")
    SEARCH_TERM = 'blugi'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/ro/ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def test_add_product_cart(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()
        self.driver.find_element(*self.BUTTON_SEARCH).click()

        query_button = (self.driver.find_element(By.CLASS_NAME, "ds-input-field-input"))
        query_button.send_keys(self.SEARCH_TERM)
        query_button.send_keys(Keys.ENTER)
        time.sleep(5)

        select_product = self.driver.find_element(By.CLASS_NAME,"ds-product-tile-img")
        select_product.click()
        time.sleep(5)

        select_size = self.driver.find_element(By.XPATH,"//span[@data-size-id='1064']")
        select_size.click()
        time.sleep(5)

        add_product = self.driver.find_element(By.XPATH,"//button[contains(@class,'gPVJln')]")
        add_product.click()
        time.sleep(5)

        go_to_cart = self.driver.find_element(By.XPATH,"//a[@data-testid='cart-confirmation-go-to-cart']")
        go_to_cart.click()
        time.sleep(5)

        total_items = self.driver.find_elements(By.CLASS_NAME,"dhPdTk")

        self.assertGreater(len(total_items), 0, "Produsul nu a fost adăugat în coșul de cumpărături.")

    def tearDown(self):
        self.driver.quit()
