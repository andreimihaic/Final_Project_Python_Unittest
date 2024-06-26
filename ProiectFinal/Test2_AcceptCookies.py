import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAcceptCookies(unittest.TestCase):
    ACCEPT_COOKIES = (By.ID, "cookiebotDialogOkButton")

    def setUp(self):
        self.drivers = []

    def create_driver(self, browser):
        if browser == "chrome":
            self.drivers.append(webdriver.Chrome())
        elif browser == "firefox":
            self.drivers.append(webdriver.Firefox())
        elif browser == "edge":
            self.drivers.append(webdriver.Edge())
        else:
            raise ValueError(f"Browser necunoscut: {browser}")

        self.drivers[-1].get("https://www.sinsay.com/")
        self.drivers[-1].maximize_window()
        self.drivers[-1].implicitly_wait(5)

    def test_accept_cookies(self):
        browsers = ["chrome", "firefox", "edge"]
        for browser in browsers:
            self.create_driver(browser)
            banner_cookies = self.drivers[-1].find_element(By.ID, "cookiebanner")
            self.drivers[-1].find_element(*self.ACCEPT_COOKIES).click()
            self.assertTrue(banner_cookies.is_enabled(), f"Banner-ul de cookies nu este afisat corect după acceptare pe {browser}.")

    def tearDown(self):
        for driver in self.drivers:
            driver.quit()
