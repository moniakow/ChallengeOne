import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPageLangToPolish(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        service=Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def testLangToPolish(self):
        user_login = LoginPage(self.driver)
        user_login.click_on_the_element(user_login.select_language_dropdown_xpath)
        user_login.click_on_the_element(user_login.select_polish_dropdown_option_xpath)
        user_login.assert_element_text(self.driver, user_login.remind_password_hyperlink_xpath, user_login.expected_polish_password_remind_text)
        time.sleep(5)