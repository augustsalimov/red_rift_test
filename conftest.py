import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

DRIVERS = os.path.expanduser("~/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="ff")
    parser.addoption("--url", default="https://www.google.com")


@pytest.fixture(autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == 'ff':
        service = Service(executable_path=os.path.join(DRIVERS, "geckodriver"))
        driver = webdriver.Firefox(service=service)
    elif browser == 'chrome':
        service = Service(executable_path=os.path.join(DRIVERS, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise Exception("Driver not supported")

    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)

    def open_fun(path=""):
        return driver.get(url + path)

    driver.open = open_fun
    driver.open()
    driver.maximize_window()

    return driver
