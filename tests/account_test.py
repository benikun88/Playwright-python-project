import allure
import pytest
from pages.top_bar import TopBar



@allure.feature("Cart")
class TestMyAccount:

    @pytest.fixture(autouse=True)
    # pre steps before starting each test
    def setup_login_test(self):
        global top_bar_page
        global login_page
        global account_page
        top_bar_page = TopBar(self.page)
        login_page = top_bar_page.click_login()
        login_page.fill_info("benikun88@gmail.com", "1q2w3e4r!")
        top_bar_page.click_switch_dropdown_list_my_account()
        account_page = top_bar_page.click_my_account()

    @allure.description("Verifies that the page is loaded successfully after login.")
    def test_page_loaded(self):
        assert account_page.is_page_loaded() == True

    @allure.description("Verifies successful password change.")
    def test_password_change_successes(self):
        account_page.click_change_password_btn()
        account_page.fill_current_password("1q2w3e4r!")
        account_page.fill_new_password("1q2w3e4r!")
        account_page.fill_confirm_new_password("1q2w3e4r!")
        account_page.click_save_change()
        assert account_page.get_success_change_msg() == "You saved the account information."

    @allure.description("Verifies unsuccessful password change.")
    def test_password_change_fail(self):
        account_page.click_change_password_btn()
        account_page.fill_current_password("1q2w3e4r")
        account_page.fill_new_password("1q2w3e4r!")
        account_page.fill_confirm_new_password("1q2w3e4r!")
        account_page.click_save_change()
        assert account_page.get_fail_change_msg() == ("The password doesn't match this account. Verify the password "
                                                      "and try again.")
