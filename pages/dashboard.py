from pages.base_page import BasePage
class Dashboard(BasePage):
    main_page_xpath = "/html/body/div[2]/div[3]/div/ul[1]/div[1]/div[2]"
    players_tab_xpath = "/html/body/div[2]/div[3]/div/ul[1]/div[2]/div[2]"
    language_selector_xpath = "/html/body/div[2]/div[3]/div/ul[2]/div[1]/div[2]"
    sign_out_button_xpath = "/html/body/div[2]/div[3]/div/ul[2]/div[2]/div[2]"
    dev_team_contact_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last_created_player_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button"




