import allure
import pytest

from pages.search_page import SearchPage
from pages.top_bar import TopBar


@allure.feature("SignUp")
class TestSearch:

    @pytest.mark.parametrize("query, expected_title, expected_message", [
        ("ELISA", "Search results for: 'ELISA'", None),
        ("blablabla", None, "Your search returned no results."),
        ("Elisa", None, None)
    ])
    @allure.description("""
            Test search functionality: 
            - 'ELISA': Expecting title 'Search results for: 'ELISA''.
            - 'blablabla': Expecting message 'Your search returned no results.'
            - 'Elisa': Expecting product names containing 'Elisa'.
        """)
    def test_search(self, query, expected_title, expected_message):
        top_bar_page = TopBar(self.page)
        top_bar_page.search_for_item(query)
        search_page = SearchPage(self.page)
        if expected_title:
            assert search_page.get_search_result_page_title() == expected_title
        elif expected_message:
            assert search_page.get_no_item_results_message() == expected_message
        else:
            assert query in search_page.get_product_names()
