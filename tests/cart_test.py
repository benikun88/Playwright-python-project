import time

import allure
import pytest
from selenium.common import NoSuchElementException, WebDriverException

from pages.cart_page import CartPage
from pages.mini_cart_page import MiniCartPage
from pages.product_page import ProductPage
from pages.top_bar import TopBar
from configs import config_login
from configs import config_cart


@allure.feature("Cart")
class TestCart:

    @pytest.fixture()
    @allure.description("Setup cart for tests")
    def setup_cart(self):
        global top_bar
        global product_page
        top_bar = TopBar(self.page)
        product_page = ProductPage(self.page)
        product_page.page.goto(config_cart.PRODUCT_PAGE_URL,wait_until="load")
        product_page.choose_product_size(config_cart.PRODUCT_SIZE)
        product_page.choose_product_color(config_cart.PRODUCT_COLOR)
        product_page.click_add_to_cart()

    @pytest.fixture()
    @allure.description("Teardown cart after tests")
    def tear_down_cart(self):
        yield
        try:
            mini_cart = MiniCartPage(self.page)
            top_bar_page = TopBar(self.page)
            top_bar_page.page.goto(config_cart.HOME_PAGE_URL,wait_until="load")
            top_bar_page.click_cart_icon()
            mini_cart.remove_item()
        except TimeoutError:
            # Handle the case where the element is not found
            print("Element not found!")

    @allure.description("Test initial cart state")
    def test_initial_cart_state(self):
        time.sleep(2)
        top_bar = TopBar(self.page)
        top_bar.click_cart_icon()
        assert top_bar.get_cart_empty_msg() == config_cart.EMPTY_CART_MSG

    @pytest.mark.usefixtures("setup_cart")
    @pytest.mark.usefixtures("tear_down_cart")
    @allure.description("Test adding item to mini cart")
    def test_add_item_to_mini_cart(self):
        assert top_bar.get_mini_cart_icon_qty() == config_cart.EXPECTED_INITIAL_CART_QTY

    @pytest.mark.usefixtures("setup_cart")
    @allure.description("Test removing item from cart")
    def test_remove_item_from_cart(self):
        mini_cart_page = MiniCartPage(self.page)
        top_bar.click_cart_icon()
        mini_cart_page.remove_item()
        assert top_bar.get_cart_empty_msg() == config_cart.EMPTY_CART_MSG

    @pytest.mark.usefixtures("setup_cart")
    @pytest.mark.usefixtures("tear_down_cart")
    @allure.description("Test updating cart quantity")
    def test_update_cart_qty(self):
        assert top_bar.get_mini_cart_icon_qty() == config_cart.EXPECTED_INITIAL_CART_QTY
        product_page.click_add_to_cart()
        assert top_bar.get_mini_cart_icon_qty() == config_cart.EXPECTED_UPDATED_CART_QTY

    @pytest.mark.usefixtures("tear_down_cart")
    @allure.description("Test subtotal equals total")
    def test_sub_total_equal_total(self):
        top_bar = TopBar(self.page)
        product_page = ProductPage(self.page)
        product_page.page.goto(config_cart.PRODUCT_PAGE_URL)
        product_page.choose_product_size(config_cart.PRODUCT_SIZE)
        product_page.choose_product_color(config_cart.PRODUCT_COLOR)
        product_page.set_product_quantity(config_cart.PRODUCT_QUANTITY)
        product_page.click_add_to_cart()
        mini_cart = MiniCartPage(self.page)
        top_bar.click_cart_icon()
        # Extract numerical part of the item price
        item_price_str = mini_cart.get_item_price()
        item_price = mini_cart.convert_price_to_float(item_price_str)
        price = int(item_price) * 5
        # Convert subtotal price to numerical value
        subtotal_price_str = mini_cart.get_subtotal_price()
        subtotal_price = mini_cart.convert_price_to_float(subtotal_price_str)
        assert price == subtotal_price

    @pytest.mark.usefixtures("setup_cart")
    @pytest.mark.usefixtures("tear_down_cart")
    @allure.description("Test navigating from mini cart to cart")
    def test_navigate_from_mini_cart_to_cart(self):
        top_bar.click_cart_icon()
        mini_cart = MiniCartPage(self.page)
        mini_cart.view_cart()
        cart_page = CartPage(self.page)
        assert cart_page.is_page_loaded() == True

    @allure.description("Test quantity error message")
    def test_qty_out_of_stock_error(self):
        top_bar = TopBar(self.page)
        product_page = ProductPage(self.page)
        product_page.page.goto(config_cart.INVALID_PRODUCT_PAGE_URL)
        product_page.choose_product_size(config_cart.PRODUCT_SIZE_OUT_OF_STOCK)
        product_page.choose_product_color(config_cart.PRODUCT_COLOR_OUT_OF_STOCK)
        product_page.click_add_to_cart()
        cart_page = CartPage(self.page)
        assert cart_page.get_error_cart_msg() == config_cart.QTY_ERROR_MSG

    @pytest.mark.usefixtures("setup_cart")
    @pytest.mark.usefixtures("tear_down_cart")
    @allure.description("Test adding item to cart")
    def test_add_item_to_cart(self):
        top_bar.click_cart_icon()
        mini_cart = MiniCartPage(self.page)
        mini_cart.view_cart()
        cart=CartPage(self.page)
        assert cart.get_cart_icon_qty() == config_cart.EXPECTED_INITIAL_CART_QTY
