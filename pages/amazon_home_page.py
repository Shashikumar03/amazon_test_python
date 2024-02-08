import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AmazonHomePage:

    def __init__(self,driver):
        self.driver =driver

    def amazon_current_url(self, title, currentUrl):
        self.driver.get("https://www.amazon.in/")
        assert self.driver.title == title
        if self.driver.title == title:
            print("Title is correct")
        else:
            print("Title is not correct")
        assert self.driver.current_url == currentUrl
        if self.driver.current_url == currentUrl:
            print("current url is fine")
        else:
            print("current url is not fine")

    def validate_login(self, username, password,checkUserName):
        self.driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
        self.driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        self.driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
        text = self.driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").text
        assert text.lower().__contains__(checkUserName.lower())
        if text.lower().__contains__("shashi"):
            print("correct user is logged in")
        else:
            print("wrong user is logged in")
        try:
            assert text.lower().__contains__("vikash")
        except Exception as e:
            print("undefined user vikash")
            print(e)

    def validate_search_item(self, item_to_search, check_search):
        self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(item_to_search)
        self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        self.driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'realme GT Neo 3 (Asphalt Black, 8GB RAM, 256GB Sto')]").click()
        time.sleep(2)
        current_url = self.driver.current_url
        assert current_url.lower().__contains__(check_search)
        if current_url.lower().__contains__(check_search):
            print("search is item is matched")
        else:
            print("search is item is not matched")
        parentHandle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
