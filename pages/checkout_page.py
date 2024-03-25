import time
import allure
from playwright.sync_api import Page, ElementHandle

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_PAGE_LOAD_TITLE = ".base"
    ORDER_TOTAL = "span[data-th='Cart Subtotal']"
    DISCOUNT_PRICE = "tr[class='totals discount'] td[class='amount']"
    SHIPPING_ADDRESS_SECTION_BTN = ".shipping-address-item.selected-item"
    NEW_ADDRESS_BTN = ".action.action-show-popup"
    # Shipping Address
    FIRST_NAME_TEXT_BOX = "name=firstname"
    LAST_NAME_TEXT_BOX = "name=lastname"
    STREET_ADDRESS_TEXT_BOX = "name='street[0]'"
    CITY_TEXT_BOX = "name=city"
    COUNTRY_DROP_LIST = "name=country_id"
    ZIP_CODE = "name=postcode"
    PHONE_NUMBER_TEXT_BOX = "name=telephone"
    SHIP_HERE_BTN = "button[class='action primary action-save-address'] span"
    NEXT_BTN = ".button.action.continue.primary"
    PLACE_ORDER_BTN = "button[title='Place Order']"
    REVEL_DISCOUNT_CODE_BTN = "span[id='block-discount-heading'] span"
    DISCOUNT_CODE_FIELD = "#discount-code"
    APPLY_DISCOUNT_BTN = "button[value='Apply Discount'] "
    CANCEL_DISCOUNT_COUPON_BTN = "button[value='Cancel'] span span"
    DISCOUNT_COUPON_MSG = "div[role='alert']"
    DISCOUNT_COUPON_ERROR_MSG = "div[data-ui-id='checkout-cart-validationmessages-message-error']"
    CHECKOUT_PAGE_LOADER = "img[alt='Loading...']"
    CHECKOUT_MAIN_LOADER = "div.loading-mask"
    # account creation
    EMAIL_ADDRESS_ANONYMOUS_FIELD = ".control._with-tooltip #customer-email"
    ACCOUNT_EXISTING_NOTIFICATION = "div[class='control'] span[class='note']"
    COSTUMER_PASSWORD_FROM_ADDRESS_FIELD = "#customer-password"
    LOGIN_BTN = ".action.login.primary"
    SIGNIN_FROM_CHECKOUT_BTN = "button[class='action action-auth-toggle'] span"
    EMAIL_ADDRESS_SIGNIN_FROM_CHECKOUT_FIELD = "#login-email"
    PASSWORD_SIGNIN_FROM_CHECKOUT_FIELD = "#login-password"
    SIGN_IN_FORM = ("body > div:nth-child(5) > main:nth-child(2) > div:nth-child(3) > "
                    "div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > aside:nth-child(2) > "
                    "div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")

    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Check if the shipping address section exists")
    def is_shipping_address_section_exist(self) -> bool:
        self.page.wait_for_selector(self.SHIPPING_ADDRESS_SECTION_BTN)
        return self.is_element_exist(self.SHIPPING_ADDRESS_SECTION_BTN)

    @allure.step("Click on the 'New Address' button")
    def click_new_address_button(self):
        self.click(self.NEW_ADDRESS_BTN)

    @allure.step("Fill shipping address information")
    def fill_shipping_address(self, first_name, last_name, street_address, city, country, phone_number):
        self.fill_text(self.FIRST_NAME_TEXT_BOX, first_name)
        self.fill_text(self.LAST_NAME_TEXT_BOX, last_name)
        self.fill_text(self.STREET_ADDRESS_TEXT_BOX, street_address)
        self.fill_text(self.CITY_TEXT_BOX, city)
        self.select_by_value(self.COUNTRY_DROP_LIST, country)
        self.fill_text(self.PHONE_NUMBER_TEXT_BOX, phone_number)

    @allure.step("Fill shipping address information")
    def fill_shipping_address(self, street_address, city, country, phone_number, zip_code):
        self.fill_text(self.STREET_ADDRESS_TEXT_BOX, street_address)
        self.fill_text(self.CITY_TEXT_BOX, city)
        self.select_by_value(self.COUNTRY_DROP_LIST, country)
        self.fill_text(self.PHONE_NUMBER_TEXT_BOX, phone_number)
        self.fill_text(self.ZIP_CODE, zip_code)

    @allure.step("Click on the 'Ship Here' button")
    def click_ship_here_button(self):
        self.click(self.SHIP_HERE_BTN)

    @allure.step("Click on the 'Next' button")
    def click_next_button(self):
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        self.click(self.NEXT_BTN)

    @allure.step("Place the order")
    def click_place_order(self):
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        self.click(self.PLACE_ORDER_BTN)

    @allure.step("Check if the page is loaded")
    def is_page_loaded(self) -> bool:
        return self.is_element_exist(self.CHECKOUT_PAGE_LOAD_TITLE)

    @allure.step("Check if purchase succeeded")
    def get_purchase_msg(self) -> str:
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        return self.get_text(self.CHECKOUT_PAGE_LOAD_TITLE)

    @allure.step("Reveal the discount code section")
    def reveal_discount_code_section(self):
        time.sleep(5)
        self.click(self.REVEL_DISCOUNT_CODE_BTN)

    @allure.step("Apply a discount code: {discount_code}")
    def apply_discount_code(self, discount_code):
        self.fill_text(self.DISCOUNT_CODE_FIELD, discount_code)
        self.page.wait_for_load_state(state="load")
        self.click(self.APPLY_DISCOUNT_BTN)

    @allure.step("Cancel the applied discount code")
    def cancel_discount_code(self):
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        self.click(self.CANCEL_DISCOUNT_COUPON_BTN)

    @allure.step("Check if the discount code is applied successfully")
    def is_discount_code_applied_successfully(self) -> str:
        return self.get_text(self.DISCOUNT_COUPON_MSG)

    @allure.step("Convert price string to float: {price_str}")
    def convert_price_to_float(self, price_str: str) -> float:
        price_str = price_str.replace('$', '')
        if '.' in price_str:
            integer_part, decimal_part = price_str.split('.')
            decimal_part = decimal_part[:2]
            price_str = f"{integer_part}.{decimal_part}"
        return float(price_str)

    @allure.step("Get the total price")
    def get_total_price(self) -> str:
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        return self.get_text(self.ORDER_TOTAL)

    @allure.step("Get the total price")
    def get_discount_amount(self) -> str:
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER, state="hidden")
        return self.get_text(self.DISCOUNT_PRICE)

    @allure.step("Fill email address field for anonymous account creation")
    def fill_anonymous_email_address(self, email_address: str):
        self.fill_text(self.EMAIL_ADDRESS_ANONYMOUS_FIELD, email_address)

    @allure.step("Fill password field for anonymous account creation")
    def fill_customer_password(self, password: str):
        self.fill_text(self.COSTUMER_PASSWORD_FROM_ADDRESS_FIELD, password)

    @allure.step("Click on the login button")
    def click_login_button(self):
        self.click(self.LOGIN_BTN)

    @allure.step("Click on the Sign-in from checkout button")
    def click_signin_from_checkout_button(self):
        self.page.wait_for_selector(self.CHECKOUT_PAGE_LOADER,state="hidden")
        self.click(self.SIGNIN_FROM_CHECKOUT_BTN)

    @allure.step("Fill email address field for sign-in from checkout")
    def fill_email_address_signin_from_checkout(self, email_address: str):
        self.fill_text(self.EMAIL_ADDRESS_SIGNIN_FROM_CHECKOUT_FIELD, email_address)

    @allure.step("Fill password field for sign-in from checkout")
    def fill_password_signin_from_checkout(self, password: str):
        self.fill_text(self.PASSWORD_SIGNIN_FROM_CHECKOUT_FIELD, password)

    @allure.step("Get the sign in form section for visual testing")
    def get_sign_in_form_section(self) -> ElementHandle:
        return self.page.wait_for_selector(self.SIGN_IN_FORM,state="hidden")

