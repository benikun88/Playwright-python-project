import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class AccountPage(BasePage):
    # Locators for elements on the page
    EDIT_BTN = 'div.box.box-information a.action.edit'
    CHANGE_PASSWORD_BTN = '.action.change-password'
    MANAGE_ADDRESS_BTN = 'body > div:nth-child(5) > main:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > a:nth-child(2) > span:nth-child(1)'
    EDIT_ADDRESS_BTN = 'a[data-ui-id="default-billing-edit-link"] span'
    # address locators
    STREET_ADDRESS_TEXT_BOX = '#street_1'
    CITY_TEXT_BOX = '#city'
    COUNTRY_DROP_LIST = '#country'
    ZIP_CODE = '#zip'
    PHONE_NUMBER_TEXT_BOX = '#telephone'
    SAVE_ADDRESS_BTN = 'button[title="Save Address"] span'

    ORDER_STATUS_COL = '.col.status'
    VIEW_ORDER = '.action.view'
    REORDER_ORDER = '.action.order'
    FIRST_NAME_TEXT_BOX = '#firstname'
    LAST_NAME_TEXT_BOX = '#lastname'
    EMAIL_TEXT_BOX = '#email'
    CURRENT_PASSWORD_TEXT_BOX = '#current-password'
    NEW_PASSWORD_TEXT_BOX = '#password'
    CONFIRM_NEW_PASSWORD_TEXT_BOX = '#password-confirmation'
    EMAIL_CHANGE_CHECK_BOX = '#change-email'
    PASSWORD_CHANGE_CHECK_BOX = '#change-password'
    SAVE_CHANGE_BTN = 'button[title="Save"]'
    MY_ORDERS_SECTION = 'div.sidebar.sidebar-main li:nth-child(2) a:nth-child(1)'
    ACCOUNT_UPDATE_INFO_MSG = '.message-success.success.message div'
    ACCOUNT_UPDATE_INFO_MSG_ERROR = '.message-error.error.message'
    ACCOUNT_PAGE_LOAD_TITLE = '.base'

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Check if account page is loaded")
    def is_page_loaded(self):
        return self.is_elements_exist(self.ACCOUNT_PAGE_LOAD_TITLE)

    # Clicks the "Edit" button
    @allure.step("Click the Edit button")
    def click_edit_btn(self):
        self.click(self.EDIT_BTN)

    @allure.step("Click the Change Password button")
    def click_change_password_btn(self):
        self.click(self.CHANGE_PASSWORD_BTN)

    @allure.step("Click the Manage Address button")
    def click_manage_address_btn(self):
        self.click(self.MANAGE_ADDRESS_BTN)

    @allure.step("Fill the first name in the form: {first_name}")
    def fill_name(self, first_name):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)

    @allure.step("Fill the last name in the form: {last_name}")
    def fill_last_name(self, last_name):
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)

    @allure.step("Fill the current password in the form: {current_pass}")
    def fill_current_password(self, current_pass):
        self.fill_text(self.CURRENT_PASSWORD_TEXT_BOX, current_pass)

    @allure.step("Fill the new password in the form: {new_pass}")
    def fill_new_password(self, new_pass):
        self.fill_text(self.NEW_PASSWORD_TEXT_BOX, new_pass)

    @allure.step("Fill the confirmation of the new password in the form: {confirm_pass}")
    def fill_confirm_new_password(self, confirm_pass):
        self.fill_text(self.CONFIRM_NEW_PASSWORD_TEXT_BOX, confirm_pass)

    @allure.step("Check the 'Change Email' checkbox")
    def check_email_change_checkbox(self):
        self.click(self.EMAIL_CHANGE_CHECK_BOX)

    @allure.step("Fill the email in the form: {email}")
    def fill_email(self, email):
        self.fill_text(self.EMAIL_TEXT_BOX, email)

    @allure.step("Check the 'Change Password' checkbox")
    def check_password_change_checkbox(self):
        self.click(self.PASSWORD_CHANGE_CHECK_BOX)

    @allure.step("Click the 'Save Changes' button")
    def click_save_change(self):
        self.click(self.SAVE_CHANGE_BTN)

    @allure.step("Retrieve the success change message")
    def get_success_change_msg(self):
        return self.get_text(self.ACCOUNT_UPDATE_INFO_MSG)

    @allure.step("Retrieve the fail change message")
    def get_fail_change_msg(self):
        return self.get_text(self.ACCOUNT_UPDATE_INFO_MSG_ERROR)

    @allure.step("Retrieve the successful registration text message")
    def get_successful_registration_text_msg(self):
        return self.get_text(self.ACCOUNT_UPDATE_INFO_MSG)

    @allure.step("Click edit address Btn")
    def click_edit_address_btn(self):
        return self.click(self.EDIT_ADDRESS_BTN)

    @allure.step("Fill shipping address information")
    def fill_shipping_address(self, street_address, city, country, phone_number, zip_code):
        # self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)
        # self.fill_text(self.LAST_NAME_TEXT_BOX,
        #                )
        self.fill_text(self.STREET_ADDRESS_TEXT_BOX, street_address)
        self.fill_text(self.CITY_TEXT_BOX, city)
        self.select_by_value(self.COUNTRY_DROP_LIST, country)
        self.fill_text(self.PHONE_NUMBER_TEXT_BOX, phone_number)
        self.fill_text(self.ZIP_CODE, zip_code)

    @allure.step("Click save Address")
    def click_save_address(self):
        return self.click(self.SAVE_ADDRESS_BTN)
