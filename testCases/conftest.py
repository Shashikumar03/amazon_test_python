import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import logging
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_option = request.config.getoption("--browser")

    if browser_option == "chrome":
        service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_option == "firefox":

        service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/geckodriver.exe')
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Invalid browser option")

    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep_' + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")
