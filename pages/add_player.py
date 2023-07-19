import time
from pages.base_page import BasePage

class AddPlayer(BasePage):
    add_player_header_xpath = '//*[@id="__next"]//form/div[1]/div/span'
    new_player_email_input_xpath = '//*[@id="__next"]//div[1]/div/div/input'
    new_player_name_input_xpath = '//*[@id="__next"]//div[2]/div/div/input'
    new_player_surname_input_xpath = '//*[@id="__next"]//div[3]/div/div/input'
    new_player_weight_input_xpath = '//*[@id="__next"]//div[5]/div/div/input'
    new_player_height_input_xpath = '//*[@id="__next"]//div[6]/div/div/input'
    new_player_age_input_xpath = '//*[@id="__next"]//div[7]/div/div/input'
    new_player_select_right_leg_xpath = '//*[@id="menu-leg"]//li[1]'
    new_player_select_left_leg_xpath = '//*[@id="menu-leg"]//li[2]'
    new_player_club_input_xpath = '//*[@id="__next"]//div[9]/div/div/input'
    new_player_main_position_input_xpath = '//*[@id="__next"]//div[11]/div/div/input'
    new_player_select_district_lodz_xpath = '//div[2]/div[3]/ul/li[5]'
    new_player_leg_dropdown_xpath = '//*[@id="mui-component-select-leg"]'
    new_player_select_district_dropdown_xpath = '//*[@id="mui-component-select-district"]'
    edit_newly_created_player_header_xpath = '//div[2]/form/div[1]/div/span'
    newly_created_player_xpath = '/html/body/div/div[1]/div/div/div/ul[2]/div[1]/div[2]/span'
    add_link_to_youtube_button_xpath = ''
    remove_link_to_youtube_button_xpath = ''
    submit_form_button_xpath = '/html/body/div/div[1]/main/div[2]/form/div[3]/button[1]'
    main_page_button_xpath = '/html/body/div/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    expected_page_header = "Add player"
    expected_edit_new_player_header = "Edit player Bronek Bomba"
    expected_newly_created_player = "Bronek Bomba"

    def header_of_page(self):
        assert self.get_element_text(self.add_player_header_) == self.expected_page_header

    def select_leg(self, leg):
        self.click_on_the_element(self.new_player_leg_dropdown_xpath)
        time.sleep(1)
        if leg == "right":
            self.click_on_the_element(self.new_player_select_right_leg_xpath)
        else:
            self.click_on_the_element(self.new_player_select_left_leg_xpath)
            time.sleep(5)