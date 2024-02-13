import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import logging

from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope="class")
def setup(request):

    service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
    options = webdriver.ChromeOptions()
    global  driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="function", autouse=True)
def log_on_failure(request):
    yield
    item=request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item,'rep_'+rep.when, rep)
    return rep


