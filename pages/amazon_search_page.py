import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AmazonSearchedPage:
    def __init__(self, driver):
        self.driver = driver

    def validate_selected_item(self):
        print(self.driver.current_url)
        try:
            dropDown = self.driver.find_element(By.XPATH, "//select[@id='quantity']")
            if dropDown.is_displayed():
                dd = Select(dropDown)
                dd.select_by_value("2")
        except NoSuchElementException as e:
            print("An exception occurred")

        # print(dropDown.is_displayed())

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='buy-now-button']").click()
        time.sleep(5)

    def validate_payment_page(self, checkoutText, address):
        checkout = self.driver.find_element(By.XPATH,"//h1[normalize-space()='Checkout']").text
        assert checkout.lower().__contains__(checkoutText)
        delivery_address = self.driver.find_element(By.XPATH,"//h3[@class='a-color-base clickable-heading expand-collapsed-panel-trigger']").text
        assert delivery_address.lower().__contains__(address)