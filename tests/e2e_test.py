import time

import allure
import pytest

from configs import config_login, config_signup, config_cart, config_checkout, config_account
from pages.account_page import AccountPage
from pages.checkout_page import CheckoutPage
from pages.mini_cart_page import MiniCartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar


@allure.feature("E2E")
@allure.description("E2E test")
class TestE2E:
    @allure.description("End-to-end purchase with a new account")
    def test_end_2_end_purchase_with_new_account(self):
        top_bar_page = TopBar(self.page)
        create_account = top_bar_page.click_create_account()
        create_account.sign_up(config_signup.VALID_FIRST_NAME, config_signup.VALID_LAST_NAME,
                               create_account.generate_random_email(), config_signup.VALID_PASSWORD,
                               config_signup.VALID_PASSWORD)
        account_page = AccountPage(self.page)
        account_page.click_edit_address_btn()
        account_page.fill_shipping_address(config_account.STREET_ADDRESS, config_account.CITY, config_account.COUNTRY, config_account.PHONE_NUMBER, config_account.ZIP_CODE)
        account_page.click_save_address()
        product_page = ProductPage(self.page)
        product_page.page.goto(config_cart.PRODUCT_PAGE_URL)
        product_page.choose_product_size(config_cart.PRODUCT_SIZE)
        product_page.choose_product_color(config_cart.PRODUCT_COLOR)
        product_page.click_add_to_cart()
        time.sleep(3)
        top_bar = TopBar(self.page)
        top_bar.click_cart_icon()
        mini_cart = MiniCartPage(self.page)
        mini_cart.click_proceed_checkout()
        checkout_page = CheckoutPage(self.page)
        checkout_page.click_next_button()
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code(config_checkout.VALID_DISCOUNT_CODE)
        checkout_page.click_place_order()
        assert checkout_page.get_purchase_msg() == config_checkout.EXPECTED_SUCCESS_PURCHASE_MSG

    @allure.description("End-to-end purchase with an existing account")
    @pytest.mark.xdist_group(name="serial")
    def test_end_2_end_purchase_with_exist_account(self):
        top_bar_page = TopBar(self.page)
        login_page = top_bar_page.click_login()
        login_page.fill_info(config_login.VALID_USERNAME, config_login.VALID_PASSWORD)
        product_page = ProductPage(self.page)
        product_page.page.goto(config_cart.PRODUCT_PAGE_URL)
        product_page.choose_product_size(config_cart.PRODUCT_SIZE)
        product_page.choose_product_color(config_cart.PRODUCT_COLOR)
        product_page.click_add_to_cart()
        time.sleep(2)
        top_bar = TopBar(self.page)
        top_bar.click_cart_icon()
        mini_cart = MiniCartPage(self.page)
        mini_cart.click_proceed_checkout()
        checkout_page = CheckoutPage(self.page)
        checkout_page.click_next_button()
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code(config_checkout.VALID_DISCOUNT_CODE)
        checkout_page.click_place_order()
        assert checkout_page.get_purchase_msg() == config_checkout.EXPECTED_SUCCESS_PURCHASE_MSG
