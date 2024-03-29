
import time
import pytest
from playwright.sync_api import Error
from configs import config_login, config_checkout
from pages.checkout_page import CheckoutPage
from pages.mini_cart_page import MiniCartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar
import allure


# Test class definition
@pytest.mark.xdist_group(name="serial")
@allure.feature("Checkout")
class TestCheckout:
    # Fixture for setup and teardown
    @pytest.fixture(autouse=True)
    def setup_checkout_test(self):
        """
        Setup fixture for checkout tests.
        """
        # Setup steps
        top_bar_page = TopBar(self.page)
        login_page = top_bar_page.click_login()
        login_page.fill_info(config_login.VALID_USERNAME, config_login.VALID_PASSWORD)
        time.sleep(2)
        top_bar_page.click_cart_icon()
        mini_cart = MiniCartPage(self.page)
        try:
            mini_cart.remove_item()
        except Error:
            # Handle the case where the element is not found
            print("Element not found!")
        product_page = ProductPage(self.page)
        product_page.page.goto(config_checkout.URL_ITEM_TO_ADD)
        product_page.choose_product_size(config_checkout.SIZE)
        product_page.choose_product_color(config_checkout.COLOR)
        product_page.click_add_to_cart()
        time.sleep(2)
        top_bar_page.click_cart_icon()
        mini_cart.click_proceed_checkout()
        yield
        # Teardown steps
        top_bar_page.page.goto("https://magento.softwaretestingboard.com/")
        top_bar_page.click_cart_icon()
        mini_cart.remove_item()

    # Test to apply discount code
    @allure.description("Test to apply discount code and verify the result.")
    @pytest.mark.parametrize("discount_code, expected_message", [
        (config_checkout.VALID_DISCOUNT_CODE, config_checkout.EXPECTED_SUCCESS_APPLY_CODE),
        (config_checkout.INVALID_DISCOUNT_CODE, config_checkout.EXPECTED_ERROR_INVALID_CODE),
    ])
    def test_apply_discount_code(self, discount_code, expected_message):
        checkout_page = CheckoutPage(self.page)
        checkout_page.click_next_button()
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code(discount_code)
        assert checkout_page.is_discount_code_applied_successfully() == expected_message

    # Test for discount price calculation
    @allure.description("Test to calculate the discounted price after applying a discount code.")
    def test_discount_price_calculation(self):
        checkout_page = CheckoutPage(self.page)
        checkout_page.click_next_button()
        item_price_str = checkout_page.get_total_price()
        item_price = checkout_page.convert_price_to_float(item_price_str)
        item_price_discounted = item_price * -0.2
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code(config_checkout.VALID_DISCOUNT_CODE)
        discount_price = checkout_page.convert_price_to_float(checkout_page.get_discount_amount())
        assert discount_price == item_price_discounted

    # Test to remove discount code
    @allure.description("Test to remove a discount code and verify the result.")
    def test_remove_discount_code(self):
        checkout_page = CheckoutPage(self.page)
        checkout_page.click_next_button()
        checkout_page.reveal_discount_code_section()
        checkout_page.apply_discount_code(config_checkout.VALID_DISCOUNT_CODE)
        checkout_page.cancel_discount_code()
        assert checkout_page.is_discount_code_applied_successfully() == config_checkout.EXPECTED_SUCCESS_REMOVE_CODE

    # Test to check if shipping address section exists
    @allure.description("Test to verify if the shipping address section exists.")
    def test_address_loaded(self):
        checkout_page = CheckoutPage(self.page)
        assert checkout_page.is_shipping_address_section_exist()
