import time
from pages.base_page import BasePage
class Dashboard(BasePage):
    main_page_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_tab_xpath = "/html/body/div[2]/div[3]/div/ul[1]/div[2]/div[2]"
    language_selector_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last_created_player_hyperlink_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button"

    expected_title = "Scouts panel"
    expected_last_created_player = "BRONEK BOMBA"
    expected_main_page_polish = "Strona główna"
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/')


    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_player_button_click(self):
        self.click_on_the_element(self.add_player_button_xpath)



