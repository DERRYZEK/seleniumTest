import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument("--ignore-certificate-errors")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    elif browser_name == "safari":
        driver = webdriver.Safari()

    elif browser_name == "IE":
        driver = webdriver.Ie()

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture()
def failure(request, setup):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
