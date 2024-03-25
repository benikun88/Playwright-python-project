import allure
from playwright.sync_api import Page, ElementHandle
from pages.base_page import BasePage
from pages.cart_page import CartPage


class MiniCartPage(BasePage):
    # Locators for elements on the page
    PROCEED_TO_CHECKOUT_BTN = "css=#top-cart-btn-checkout"
    CART_SUBTOTAL_PRICE = "css=span[data-bind='html: cart().subtotal_excl_tax'] span[class='price']"
    CART_ITEM_PRICE = "css=span[class='minicart-price'] span[class='price']"
    EMPTY_CART_MSG = "css=.subtitle.empty"
    REMOVE_ITEM = "css=a[title='Remove item']"
    APPROVE_REMOVE_ITEM = "css=.action-primary.action-accept"
    VIEW_EDIT_BTN = "css=.action.viewcart"
    UPDATE_BTN = "css=.update-cart-item"
    QTY_TEXTBOX = "css=.item-qty.cart-item-qty"
    CLOSE_MINI_CART_BTN = "css=#btn-minicart-close"

    def __init__(self, page: Page):
        super().__init__(page)

    # Clicks the "Proceed to Checkout" button in the mini cart and returns a new CartPage instance
    @allure.step("Click 'Proceed to Checkout' button in the mini cart")
    def click_proceed_checkout(self) -> CartPage:
        self.page.click(self.PROCEED_TO_CHECKOUT_BTN)
        return CartPage(self.page)

    # Retrieves the item price from the mini cart
    @allure.step("Get item price from the mini cart")
    def get_item_price(self) -> str:
        return self.get_text(self.CART_ITEM_PRICE)

    # Retrieves the subtotal price from the mini cart
    @allure.step("Get subtotal price from the mini cart")
    def get_subtotal_price(self) -> str:
        return self.get_text(self.CART_SUBTOTAL_PRICE)

    # Retrieves the empty cart message from the mini cart
    @allure.step("Get empty cart message from the mini cart")
    def get_cart_empty_msg(self) -> str:
        return self.get_text(self.EMPTY_CART_MSG)

    # Fills the quantity in the mini cart and updates it
    @allure.step("Fill quantity in the mini cart and update it")
    def fill_quantity(self, qty: str):
        qty_input = self.page.locator(self.QTY_TEXTBOX)
        qty_input.fill(qty)
        self.click(self.UPDATE_BTN)

    # Removes an item from the mini cart
    @allure.step("Remove an item from the mini cart")
    def remove_item(self):
        self.page.wait_for_selector(self.REMOVE_ITEM,timeout=10000)
        self.click(self.REMOVE_ITEM)
        self.click(self.APPROVE_REMOVE_ITEM)
        self.page.wait_for_timeout(3000)

    # Views the cart in the mini cart
    @allure.step("View the cart in the mini cart")
    def view_cart(self):
        self.click(self.VIEW_EDIT_BTN)

    # Clicks the "Close Mini Cart" button
    @allure.step("Click 'Close Mini Cart' button")
    def close_mini_cart(self):
        self.click(self.CLOSE_MINI_CART_BTN)

    # Converts a price string to a floating-point number
    @allure.step("Converts a price string to a floating-point number")
    def convert_price_to_float(self, price_str: str) -> float:
        return float(price_str.replace('$', ''))
