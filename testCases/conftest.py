import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
@pytest.fixture(scope="class")
def setup(request):
    service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()