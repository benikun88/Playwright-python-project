import pytest
from _pytest.config import Config

import allure

from applitools.selenium import Eyes


@pytest.fixture(autouse=True)
def setup(request, playwright):
    if "api" not in request.node.keywords:
        global page
        global browser
        browser = playwright.chromium.launch(headless=True)
        # context = browser.new_context(viewport=None, is_mobile=False)
        page = browser.new_page()
        # Set the viewport size to simulate maximizing the browser window
        # page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto("https://magento.softwaretestingboard.com/")
        request.cls.page = page  # Provide the page object to the test class
        get_started_link = page.locator("div[class='panel header'] li[data-label='or'] a")
        # get_started_link.click()
        yield
        browser.close()
    else:
        yield None


def pytest_exception_interact(report):
    if report.failed:
        if "api" not in report.keywords:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"


@pytest.fixture()
def eyes():
    eyes = Eyes()
    eyes.api_key = 'yQZoWxzsvOfSFbrd3YGmcSpl1061UWFGuNz6dXPWMQvXA110'  # Set your Applitools API key here
    yield eyes
    eyes.abort_async()  # Make sure to abort the session to handle any exceptions

# def pytest_sessionfinish() -> None:
#     environment_properties = {
#      'browser': driver.name,
#      'driver_version': driver.capabilities['browserVersion']
#     }
#     allure_env_path = os.path.join("allure-results", 'environment.properties')
#     with open(allure_env_path, 'w') as f:
#         data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
#         f.write(data)
