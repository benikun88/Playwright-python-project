# configs/config_checkout.py

# Test data for checkout
VALID_DISCOUNT_CODE = "20poff"
INVALID_DISCOUNT_CODE = "20pof"

# Expected success and error messages for discount code
EXPECTED_SUCCESS_APPLY_CODE = "Your coupon was successfully applied."
EXPECTED_SUCCESS_REMOVE_CODE = "Your coupon was successfully removed."
EXPECTED_ERROR_INVALID_CODE = "The coupon code isn't valid. Verify the code and try again."
EXPECTED_SUCCESS_PURCHASE_MSG = "Thank you for your purchase!"
# Test URLs
CHECKOUT_PAGE_URL = "https://magento.softwaretestingboard.com/checkout"
URL_ITEM_TO_ADD = "https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html#"
MAIN_PAGE_URL = "https://magento.softwaretestingboard.com/"
# Other configurations
WAIT_TIME = 10  # Adjust this according to your needs
SIZE = "S"
COLOR = "Black"

# address
STREET_ADDRESS = "test"
CITY = "Tel Aviv"
COUNTRY = "IL"
PHONE_NUMBER = "0521119191"
ZIP_CODE = "1231231"