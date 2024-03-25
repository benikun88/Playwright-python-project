from playwright.sync_api import Page, Locator, ElementHandle
import random
import string


class BasePage:
    """ Wrapper for playwright operations """

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str) -> None:
        el: locator = self.page.locator(locator)
        el.evaluate('(element) => element.style.border = "1px solid blue"')
        el.click()

    def fill_text(self, locator: str, txt: str) -> None:
        self.page.wait_for_selector(locator)
        el: locator = self.page.locator(locator)
        el.evaluate('(element) => element.style.border = "1px solid blue"')
        el.fill(txt, no_wait_after=False)

    def fill_text_without_clean(self, locator, txt: str) -> None:
        self.page.wait_for_selector(locator)
        el: locator = self.page.locator(locator)
        el.evaluate('(element) => element.style.border = "1px solid blue"')
        el.press('Space')

    def get_text(self, locator: str) -> str:
        el: locator = self.page.locator(locator)
        return el.text_content().strip()

    def get_text_from_attribute(self, locator: str, attribute_name='text') -> str:
        el: locator = self.page.locator(locator)
        return el.get_attribute(attribute_name)

    # //need to be in utils app
    def generate_random_email(self) -> str:
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        domain = "gmail.com"
        email = f"{username}@{domain}"
        return email

    def select_by_value(self, locator: str, value):
        el = self.page.locator(locator)
        el.select_option(value)

    def select_by_text(self, locator: str, text):
        el = self.page.locator(locator)
        el.select_text()

    def select_by_index(self, locator: str, index):
        el = self.page.locator(locator)
        el.select_option({'index': index})

    def is_elements_exist(self, locator: str):
        try:
            return len(self.page.locator(locator).all()) > 0
        except Exception as e:
            return False

    def is_elements_dont_exist(self, locator: str):
        try:
            return not self.page.locator(locator).all()
        except Exception as e:
            return False

    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.page.goto(url)

    def find_elements(self, locator: str):
        """
        Find multiple elements based on locator.
        Args:
            locator (str): CSS selector.

        Returns:
            list: A list of web elements matching the given locator.
        """
        return self.page.locator(locator).all()

    def is_element_visible(self, selector: str) -> bool:
        """
        Check if an element specified by the CSS selector is visible on the page.

        Args:
            selector (str): The CSS selector of the element to check.

        Returns:
            bool: True if the element is visible, False otherwise.
        """
        try:
            element = self.page.query_selector(selector)
            if element:
                return element.is_visible()
            else:
                return False
        except Exception:
            return False

    def is_element_exist(self, selector: str) -> bool:
        """
        Check if an element specified by the CSS selector exists on the page.

        Args:
            selector (str): The CSS selector of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            element = self.page.query_selector(selector)
            return bool(element)
        except Exception:
            return False
