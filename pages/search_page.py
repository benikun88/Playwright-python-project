from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class SearchPage(BasePage):
    PRODUCT_NAME = ".product-item-link"
    NO_ITEM_RESULTS_IN_SEARCH_MSG = ".message.notice"
    SEARCH_RESULT_PAGE_TITLE = ".base"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get product names")
    def get_product_names(self):
        element = self.page.query_selector(self.PRODUCT_NAME)
        if element:
            return element.text_content().strip()
        else:
            return None

    @allure.step("Get no item results message")
    def get_no_item_results_message(self):
        return self.get_text(self.NO_ITEM_RESULTS_IN_SEARCH_MSG)

    @allure.step("Get search result page title")
    def get_search_result_page_title(self):
        return self.get_text(self.SEARCH_RESULT_PAGE_TITLE)
