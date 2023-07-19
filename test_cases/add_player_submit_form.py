import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerSubmitForm(unittest.TestCase):

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

    def testSubmitPlayerForm(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user03@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.submit_password()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_element(dashboard_page.add_player_button_xpath)
        add_player_page = AddPlayer(self.driver)
        add_player_page.field_send_keys(add_player_page.new_player_email_input_xpath, "test1@yahoo.com")
        add_player_page.field_send_keys(add_player_page.new_player_name_input_xpath, "Bronek")
        add_player_page.field_send_keys(add_player_page.new_player_surname_input_xpath, "Bomba")
        add_player_page.field_send_keys(add_player_page.new_player_weight_input_xpath, "56 kg")
        add_player_page.field_send_keys(add_player_page.new_player_height_input_xpath, "165 cm")
        add_player_page.field_send_keys(add_player_page.new_player_age_input_xpath, "21.04.1998")
        add_player_page.click_on_the_element(add_player_page.new_player_leg_dropdown_xpath)
        add_player_page.click_on_the_element(add_player_page.new_player_select_right_leg_xpath)
        add_player_page.field_send_keys(add_player_page.new_player_main_position_input_xpath, "standing")
        add_player_page.click_on_the_element(add_player_page.new_player_select_district_dropdown_xpath)
        add_player_page.click_on_the_element(add_player_page.new_player_select_district_lodz_xpath)
        add_player_page.click_on_the_element(add_player_page.submit_form_button_xpath)
        add_player_page.click_on_the_element(add_player_page.main_page_button_xpath)
        time.sleep(10)
        dashboard_page_2 = Dashboard(self.driver)
        dashboard_page_2.assert_element_text(self.driver, dashboard_page_2.last_created_player_hyperlink_xpath, dashboard_page_2.expected_last_created_player)
        time.sleep(10)