import time
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_PRICE = "span(id='product-price-1812') span(class='price')"
    PRODUCT_SIZE_LIST = ".swatch-option.text"
    PRODUCT_COLOR_LIST = ".swatch-option.color"
    PRODUCT_QTY = "#qty"
    ADD_TO_CART_BTN = "#product-addtocart-button"
    CHOSEN_SIZE = "div(class='swatch-attribute size') span(class='swatch-attribute-selected-option')"
    ADD_TO_COMPARE_LOGO = "div(class='product-addto-links') a(class='action tocompare')"
    ADD_TO_WISH_LIST_LOGO = "div(class='product-addto-links') a(class='action towishlist')"
    CHOSEN_COLOR = ".swatch-option.color.selected"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get product price")
    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    @allure.step("Choose product size")
    def choose_product_size(self, size):
        self.page.wait_for_selector(self.PRODUCT_SIZE_LIST)
        size_elements = self.page.query_selector_all(self.PRODUCT_SIZE_LIST)
        print(size_elements)
        for size_element in size_elements:
            if size_element.get_attribute("option-label") == size:
                size_element.click()
                return

    @allure.step("Choose product color")
    def choose_product_color(self, color):
        self.page.wait_for_selector(self.PRODUCT_COLOR_LIST)
        color_elements = self.page.query_selector_all(self.PRODUCT_COLOR_LIST)
        for color_element in color_elements:
            if color_element.get_attribute("option-label") == color:
                color_element.click()
                return

    @allure.step("Set product quantity")
    def set_product_quantity(self, quantity):
        self.fill_text(self.PRODUCT_QTY, str(quantity))

    @allure.step("Click add to cart")
    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        time.sleep(2)

    @allure.step("Get chosen size")
    def get_chosen_size(self):
        return self.get_text(self.CHOSEN_SIZE)

    @allure.step("Get chosen color")
    def get_chosen_color(self):
        return self.get_text(self.CHOSEN_COLOR)

    @allure.step("Get compare logo")
    def get_compare_logo(self):
        return self.page.locator(self.ADD_TO_COMPARE_LOGO)

    @allure.step("Get wish list logo")
    def get_wish_list_logo(self):
        return self.page.locator(self.ADD_TO_WISH_LIST_LOGO)
