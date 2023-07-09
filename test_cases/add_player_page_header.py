import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPageHeader(unittest.TestCase):
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

    def test_user_login(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user03@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.submit_password()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.add_player_button_click()
        add_player_page = AddPlayer(self.driver)
        add_player_page.header_of_page()
        time.sleep(5)