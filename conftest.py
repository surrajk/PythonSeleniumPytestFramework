import time
import pytest
from selenium import webdriver


# pytest terminal option registration
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",  # or "store_true", "store_false", etc.
        default="chrome",
        help="browser selection",
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        time.sleep(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(time_to_wait=5)
        time.sleep(5)
    elif browser_name == "edge":
        driver = webdriver.Ie()
        driver.implicitly_wait(5)
        time.sleep(5)

    yield driver
    driver.close()