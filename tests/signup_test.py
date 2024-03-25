import time
import allure
import pytest
from configs import config_signup
from pages.top_bar import TopBar


@allure.feature("SignUp")
class TestSignUp:
    @allure.description("""
        Test successful user signup.

        Steps:
        1. Click on the 'Create Account' link.
        2. Fill in the signup form with valid data.
        3. Verify successful registration message.
    """)
    def test_successful_signup(self):
        top_bar_page = TopBar(self.page)
        create_account = top_bar_page.click_create_account()
        account_page = create_account.sign_up(config_signup.VALID_FIRST_NAME, config_signup.VALID_LAST_NAME,
                                              create_account.generate_random_email(), config_signup.VALID_PASSWORD,
                                              config_signup.VALID_PASSWORD)
        time.sleep(5)
        assert account_page.get_successful_registration_text_msg() == "Thank you for registering with Main Website Store."

    # test existing user
    @allure.description("""
        Test user signup with an existing email address.

        Steps:
        1. Click on the 'Create Account' link.
        2. Fill in the signup form with an email address that already exists.
        3. Verify the error message indicating the existing user.
    """)
    def test_existing_user_signup(self):
        top_bar_page = TopBar(self.page)
        create_account = top_bar_page.click_create_account()
        create_account.sign_up(config_signup.VALID_FIRST_NAME, config_signup.VALID_LAST_NAME,
                               config_signup.EXISTING_EMAIL,
                               config_signup.VALID_PASSWORD, config_signup.VALID_PASSWORD)
        time.sleep(5)
        assert create_account.get_existing_user_error() == config_signup.EXISTING_USER_ERROR_MESSAGE

    @allure.description("""
        Test user signup with an invalid email address.

        Steps:
        1. Click on the 'Create Account' link.
        2. Fill in the signup form with an invalid email address.
        3. Verify the error message indicating an invalid email address.
    """)
    def test_invalid_email_signup(self):
        top_bar_page = TopBar(self.page)
        create_account = top_bar_page.click_create_account()

        # Fill in the signup form with invalid email
        create_account.sign_up(config_signup.VALID_FIRST_NAME, config_signup.VALID_LAST_NAME,
                               config_signup.INVALID_EMAIL,
                               config_signup.VALID_PASSWORD, config_signup.VALID_PASSWORD)
        # Verify the error message for the email field
        error_message = create_account.get_field_errors("email")
        assert error_message == config_signup.INVALID_EMAIL_ERROR_MESSAGE

    @pytest.mark.devRun
    def test_page_loaded(self):
        top_bar_page = TopBar(self.page)
        account_page = top_bar_page.click_create_account()
        assert account_page.is_page_loaded() == True
