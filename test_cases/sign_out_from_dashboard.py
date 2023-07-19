import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class SignOutDashboard(unittest.TestCase):

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

    def testLogoutDashboard(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user05@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.submit_password()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_element(dashboard_page.sign_out_button_xpath)
        user_login_2 = LoginPage(self.driver)
        user_login_2.assert_element_text(self.driver, user_login_2.login_header_xpath, user_login_2.expected_login_header)