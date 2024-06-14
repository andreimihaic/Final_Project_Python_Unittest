import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ReturnHomepage(unittest.TestCase):
    locators = {
        "ACCEPT_COOKIES": (By.ID, "cookiebotDialogOkButton"),
        "HANDLE_BUTTON": (By.XPATH, '//a[text()="Du-te la magazin"]'),
        "BUTTON_SEARCH": (By.ID, "algoliaButton"),
        "QUERY_BUTTON": (By.CLASS_NAME, "ds-input-field-input")
    }

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/ro/ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_return_homepage(self):
        self.driver.find_element(*self.locators["ACCEPT_COOKIES"]).click()
        self.driver.find_element(*self.locators["BUTTON_SEARCH"]).click()
        self.driver.find_element(*self.locators["QUERY_BUTTON"]).send_keys("tricouri")
        button_brand_log = self.driver.find_element(By.ID, "brandLogo")
        button_brand_log.click()

        if self.driver.current_url == "https://www.sinsay.com/ro/ro/":
            print('Test passed: Ne-am intors pe pagina principala.')
        else:
            print('Test failed: Nu am reusit sa ne intoarcem pe pagina principala.')

        self.assertTrue("www.sinsay.com" in self.driver.current_url,
                        'Nu am reusit sa ne intoarcem pe pagina principala.')

    def tearDown(self):
        self.driver.quit()
