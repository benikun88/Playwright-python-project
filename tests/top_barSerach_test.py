import allure
import pytest

from pages.top_bar import TopBar


@allure.feature("Top bar")
class TestTopBar:

    @allure.description("Verify the visibility of the site logo")
    def test_logo_visibility(self):
        top_bar = TopBar(self.page)
        assert top_bar.is_logo_visible(), "The site logo is not present or visible."

    @allure.description("Verify that the top bar persists across different pages")
    def test_top_bar_persists(self):
        top_bar = TopBar(self.page)
        pages_to_visit = ["/customer/account/login", "/customer/account/create/", "/sale.html"]
        for page in pages_to_visit:
            self.page.goto(f"https://magento.softwaretestingboard.com{page}")
            assert top_bar.is_top_bar_visible(), f"The top bar is not visible on the {page} page."

    @allure.description("Verify that the search bar persists across different pages")
    def test_search_bar_persists(self):
        top_bar = TopBar(self.page)
        pages_to_visit = ["/customer/account/login", "/customer/account/create/", "/sale.html"]
        for page in pages_to_visit:
            self.page.goto(f"https://magento.softwaretestingboard.com{page}")
            assert top_bar.is_search_bar_visible(), f"The search bar is not visible on the {page} page."
