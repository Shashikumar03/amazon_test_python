import time

import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from error_message.error import ErrorMessage


class AmazonSearchedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def amazon_current_url(self, title, currentUrl):
        self.driver.get("https://www.amazon.in/")

    def validate_selected_item(self):
        print(self.driver.current_url)
        try:
            dropDown = self.driver.find_element(By.XPATH, "//select[@id='quantity']")
            if dropDown.is_displayed():
                dd = Select(dropDown)
                dd.select_by_value("2")
        except NoSuchElementException as e:
            print("An exception occurred")
            allure.attach(self.driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)

        # print(dropDown.is_displayed())

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='buy-now-button']").click()
        time.sleep(5)

    def validate_payment_page(self, checkoutText, address):
        checkout = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Checkout']").text
        assert checkout.lower().__contains__(checkoutText)
        delivery_address = self.driver.find_element(By.XPATH,
                                                    "//h3[@class='a-color-base clickable-heading "
                                                    "expand-collapsed-panel-trigger']").text
        # assert fail
        assert delivery_address.lower().__contains__(address)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Code']").send_keys("discount")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='ppw-claimCodeApplyPressed']").click()
        coupon_failed_test = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//p[normalize-space()='The promotional code you entered is not valid.']"))).text.lower()
        assert coupon_failed_test == ErrorMessage.invalid_coupon
