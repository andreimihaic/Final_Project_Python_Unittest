import unittest
from selenium import webdriver


class TestWebsiteOpen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sinsay.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_open_website(self):
        expected_title = "Select your country - Sinsay - Great fashion, Great prices!"
        actual_title = self.driver.title

        self.assertEqual(expected_title, actual_title, f"Expected title: {expected_title}, Actual title: {actual_title}")

    def tearDown(self):
        self.driver.quit()
