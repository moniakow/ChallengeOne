from pages.base_page import BasePage

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//parent::button/span[1]"
    login_header_xpath = "//*[@id='__next']//div[1]/h5"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    select_language_dropdown_xpath = '//form/div/div[2]/div'
    select_polish_dropdown_option_xpath = '//div[3]/ul/li[1]'
    remind_password_hyperlink_xpath = '//div[1]/a'
    password_invalid_info_xpath = '/html/body/div/form/div/div[1]/div[3]/span'
    expected_login_header = "Scouts Panel"
    expected_polish_password_remind_text = "Przypomnij hasło"
    expected_invalid_password_message = "Identifier or password invalid."


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def submit_password(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
