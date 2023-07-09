import time
from pages.base_page import BasePage

class AddPlayer(BasePage):
    add_player_header = '//*[@id="__next"]//form/div[1]/div/span'
    expected_page_header = "Add player"
    def header_of_page(self):
        assert self.get_element_text(self.add_player_header) == self.expected_page_header