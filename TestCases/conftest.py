import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    options.udid = 'b4c0762b'
    options.app_package = 'com.booking'
    options.app_activity = 'com.booking.startup.HomeActivity'
    options.auto_grant_permissions = True
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
