import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators for elements on the page
    LOGIN_PAGE_LOAD_TITLE = ".base"
    EMAIL_FIELD = "#email"
    PASSWORD_FIELD = "input[name='login[password]']"
    CLICK_BTN = ".action.login.primary"
    CLICK_LOGIN = "div[class='panel header'] li[data-label='or'] a"
    EMAIL_FIELD_ERROR = "#email-error"
    PASSWORD_FIELD_ERROR = "#pass-error"
    WRONG_SIGNIN_ERROR = ".message-error.error.message"
    MY_ACCOUNT_BTN = "div[class='panel header'] li[class='greet welcome']"
    FORGOT_PASSWORD_BTN = "a[class='action remind'] span"
    RESET_MY_PASSWORD_BTN = ".action.submit.primary"
    EMAIL_RESET_FIELD = "#email_address"
    ACCOUNT_ASSOCIATED_INFO_MSG = ".message-success.success.message div"
    EMAIL_TEXT_BOX_ERROR = "#email_address-error"

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Fill login information - Email: {email}, Password: {password}")
    def fill_info(self, email, password):
        # Fill email field
        self.fill_text(self.EMAIL_FIELD, email)
        # Fill password field
        self.fill_text(self.PASSWORD_FIELD, password)
        # Click the login button
        self.page.wait_for_selector(self.CLICK_BTN)
        self.click(self.CLICK_BTN)

    @allure.step("Retrieve email error message")
    def get_email_error(self):
        # Return the text of the email error element
        return self.get_text(self.EMAIL_FIELD_ERROR)

    @allure.step("Retrieve email textbox error message")
    def get_email_checkbox_error(self):
        # Return the text of the email error element
        return self.get_text(self.EMAIL_TEXT_BOX_ERROR)

    @allure.step("Retrieve password error message")
    def get_password_error(self):
        # Return the text of the password error element
        return self.get_text(self.PASSWORD_FIELD_ERROR)

    @allure.step("Retrieve success login message")
    def get_success_login(self):
        # Return the text of the my account button (indicating a successful login)
        return self.get_text(self.MY_ACCOUNT_BTN)

    @allure.step("Check if LoginPage is loaded")
    def is_page_loaded(self):
        return self.is_element_visible(self.LOGIN_PAGE_LOAD_TITLE)

    @allure.step("enter to forgot password")
    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_BTN)

    @allure.step("fill the email address")
    def fill_email_address_reset(self, email_recover):
        self.fill_text(self.EMAIL_RESET_FIELD, email_recover)

    @allure.step("click on reset password")
    def click_reset_password(self):
        self.click(self.RESET_MY_PASSWORD_BTN)

    @allure.step("MSG of the reset process")
    def get_reset_msg_process(self):
        return self.get_text(self.ACCOUNT_ASSOCIATED_INFO_MSG)
