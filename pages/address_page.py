import time

from faker import Faker
from selenium.webdriver.common.by import By

import time

import pytest
from faker import Faker
import random
import logging

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    NAV_GLOBAL_LOCATION_POPOVER_LINK = (By.XPATH, '//a[@id=\'nav-global-location-popover-link\']')
    ADD_ADDRESS_OR_PICK_UP_POINT = (By.XPATH, "//a[normalize-space()='Add an address or pick-up point']")
    ADDRESS_TILE = (By.XPATH, "//div[@class='a-box first-desktop-address-tile']")
    FULL_NAME_INPUT = (By.ID, 'address-ui-widgets-enterAddressFullName')
    PHONE_NUMBER_INPUT = (By.ID, 'address-ui-widgets-enterAddressPhoneNumber')
    POSTAL_CODE_INPUT = (By.ID, 'address-ui-widgets-enterAddressPostalCode')
    ADDRESS_LINE_INPUT = (By.ID, 'address-ui-widgets-enterAddressLine1')
    SUBMIT_BUTTON = (By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']")
    REVIEW_ADDRESS_TITLE = (By.XPATH, "//h4[normalize-space()='Review your address']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def add_new_address_with_invalid_credentials(self,fullname, mobileNumber, pincode, flate_house,area,expected):
        url=self.driver.current_url
        print(url)
        self.driver.find_element(*self.NAV_GLOBAL_LOCATION_POPOVER_LINK).click()
        time.sleep(5)
        self.driver.find_element(*self.ADD_ADDRESS_OR_PICK_UP_POINT).click()
        time.sleep(2)
        self.driver.find_element(*self.ADDRESS_TILE).click()
        time.sleep(5)

        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(fullname)
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(mobileNumber)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(pincode)

        self.driver.find_element(*self.ADDRESS_LINE_INPUT).send_keys(area)
        self.driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-landmark']").send_keys(flate_house)

        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(10)

        print(expected)
        self.driver.get(url)


    def validate_adding_new_address_with_valid_credential(self):
        self.driver.find_element(*self.NAV_GLOBAL_LOCATION_POPOVER_LINK).click()
        time.sleep(5)
        self.driver.find_element(*self.ADD_ADDRESS_OR_PICK_UP_POINT).click()
        time.sleep(2)
        self.driver.find_element(*self.ADDRESS_TILE).click()
        time.sleep(5)
        fake = Faker('en_IN')
        list = [845305, 110001, 530068, 600001, 211001, 400001, 147301, 826124]
        first_digit = fake.random_element(elements=('1', '2', '3', '4', '5', '6', '7', '8', '9'))
        remaining_digits = fake.random_number(digits=9)
        phone_number = f"{first_digit}{remaining_digits}"
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(fake.name())
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(random.choice(list))

        self.driver.find_element(*self.ADDRESS_LINE_INPUT).send_keys(fake.address())

        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(20)
        try:
            review = self.driver.find_element(*self.REVIEW_ADDRESS_TITLE)
            if review.is_displayed():
                self.driver.find_element(*self.SUBMIT_BUTTON).click()

        except NoSuchElementException:
            print("exception")