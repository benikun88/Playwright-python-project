import time

import allure
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.signup_page import SignUpPage
from playwright.sync_api import Page


class TopBar(BasePage):
    # Locators for elements on the page
    CLICK_LOGIN = "div[class='panel header'] li[data-label='or'] a"
    CREATE_ACCOUNT_BTN = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    CART_ICON_BTN = ".action.showcart"
    CART_LOADING = "._block-content-loading"
    MINI_CART_SECTION = "#ui-id-1"
    MINI_CART_COUNTER = ".counter-number"
    CART_COUNTER_EMPTY = ".counter.qty.empty .counter-number"
    EMPTY_CART_MSG = ".subtitle.empty"
    CART_COUNTER = ".input-text.qty"
    SEARCH_TEXT_BOX = "#search"
    SEARCH_BTN = "button[title='Search']"
    TOP_BAR_ITEMS = ".level-top.ui-corner-all"
    MY_ACCOUNT_LOGGED_IN = "div[class='panel header'] span[class='logged-in']"
    MSG_DISSAPPER = "div[class='panel header'] span[class='not-logged-in']"
    SWITCH_DROP_LIST_BTN = "div[class='panel header'] button[type='button']"
    MY_ACCOUNT_BTN = "div[class='panel wrapper'] li:nth-child(1) a:nth-child(1)"
    SIGN_OUT_BTN = "div[aria-hidden='false'] li[data-label='or'] a"
    SIGN_OUT_SUCCESS_MSG = ".base"
    SITE_LOGO = "img[src='https://magento.softwaretestingboard.com/pub/static/version1695896754/frontend/Magento/luma/en_US/images/logo.svg']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    # Clicks on the login button and returns a LoginPage instance
    @allure.step("Click on the login button")
    def click_login(self):
        self.page.locator("div[class='panel header'] li[data-label='or'] a").click()
        self.click(self.CLICK_LOGIN)
        return LoginPage(self.page)

    # Waits for a success login message to appear and returns the text
    @allure.step("Wait for a success login message to appear")
    def get_success_login(self):
        time.sleep(5)  # This sleep may not be the best practice, consider using WebDriverWait instead
        return self.get_text(self.MY_ACCOUNT_LOGGED_IN)

    # Waits for the login message to disappear
    @allure.step("Wait for the login message to disappear")
    def wait_for_msg_dissaper(self):
        self.page.wait_for_selector(self.MSG_DISSAPPER, state="hidden")

    # Clicks on the "Create an Account" button and returns a SignUpPage instance
    @allure.step("Click on the 'Create an Account' button")
    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BTN)
        return SignUpPage(self.page)

    # Clicks on the shopping cart icon
    @allure.step("Click on the shopping cart icon")
    def click_cart_icon(self):
        self.page.wait_for_timeout(2000)
        self.page.wait_for_selector(self.CART_LOADING, state="hidden")
        self.click(self.CART_ICON_BTN)

    # Enters a search query in the search text box and clicks the search button
    @allure.step("Search for item: {search_query}")
    def search_for_item(self, search_query):
        self.fill_text(self.SEARCH_TEXT_BOX, search_query)
        self.page.press(self.SEARCH_TEXT_BOX,'Space')
        self.click(self.SEARCH_BTN)

    # Clicks on the switch dropdown list button
    @allure.step("Click on the switch dropdown list button")
    def click_switch_dropdown_list_my_account(self):
        time.sleep(5)
        self.click(self.SWITCH_DROP_LIST_BTN)

    # Clicks on the "My Account" button
    @allure.step("Click on the 'My Account' button")
    def click_my_account(self):
        self.click(self.MY_ACCOUNT_BTN)
        return AccountPage(self.page)

    # Clicks on the "Sign Out" button
    @allure.step("Click on the 'Sign Out' button")
    def click_sign_out(self):
        self.click(self.SIGN_OUT_BTN)

    # Enter a search query and submit the search form.
    @allure.step("Perform search for query: {query}")
    def perform_search(self, query):
        self.fill_text(self.SEARCH_TEXT_BOX, query)  # Assuming you have a fill method in BasePage

    # Click on the search button to initiate the search.
    @allure.step("Click on the search button")
    def click_search_button(self):
        self.click(self.SEARCH_TEXT_BOX)
        return SearchPage(self.page)

    @allure.step("Get success logout message")
    def get_success_logout_msg(self):
        return self.get_text(self.SIGN_OUT_SUCCESS_MSG)

    @allure.step("Check if the site logo is visible")
    def is_logo_visible(self):
        return self.is_elements_exist(self.SITE_LOGO)

    @allure.step("Check if the top bar with product types is visible")
    def is_top_bar_visible(self):
        return self.is_elements_exist(self.TOP_BAR_ITEMS)

    @allure.step("Navigate to the home page")
    def go_to_home_page(self):
        self.page.goto("https://magento.softwaretestingboard.com/")

    @allure.step("Check if the search bar is visible")
    def is_search_bar_visible(self):
        return self.is_elements_exist(self.SEARCH_TEXT_BOX)

    @allure.step("Get cart empty message")
    def get_cart_empty_msg(self):
        return self.get_text(self.EMPTY_CART_MSG)

    @allure.step("Get mini cart icon quantity")
    def get_mini_cart_icon_qty(self):
        self.page.wait_for_selector(self.CART_LOADING, state="hidden")
        return self.get_text(self.MINI_CART_COUNTER)

    @allure.step("Get cart icon quantity")
    def get_cart_icon_qty(self):
        self.page.wait_for_selector(self.CART_LOADING, state="hidden")
        return self.get_text(self.CART_COUNTER)

    @allure.step("Get cart section")
    def get_cart_section(self):
        return self.page.locator(self.MINI_CART_SECTION)
