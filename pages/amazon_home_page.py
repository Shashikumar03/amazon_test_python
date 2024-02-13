import logging
import os
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from error_message.error import ErrorMessage


class AmazonHomePage:
    NAVIGATION_MENU = (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='ap_email']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    MOBILE_ERROR_MESSAGE = (By.XPATH, "//h4[normalize-space()='Incorrect phone number']")
    GENERIC_ERROR_MESSAGE = (By.XPATH, "//h4[normalize-space()='There was a problem']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='ap_password']")
    SIGN_IN_BUTTON = (By.XPATH, "//input[@id='signInSubmit']")
    SEARCH_BOX = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def amazon_current_url(self, title):
        self.driver.get("https://www.amazon.in/")
        # false assertion
        assert self.driver.title == title



    def login_with_invalid_phone_number(self, username, expected):
        url = self.driver.current_url
        self.wait.until(EC.element_to_be_clickable(self.NAVIGATION_MENU)).click()
        # self.driver.find_element(*self.NAVIGATION_MENU).click()
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        time.sleep(2)
        try:
            mob_error_message = self.driver.find_element(*self.MOBILE_ERROR_MESSAGE).text.lower()
            assert mob_error_message == ErrorMessage.incorrect_phone_number.lower()

        except NoSuchElementException as e:
            error_message = self.driver.find_element(*self.GENERIC_ERROR_MESSAGE).text.lower()
            assert error_message == ErrorMessage.there_was_a_problem.lower()
        self.driver.get(url)




    def login_with_empty_input(self, username):
        url = self.driver.current_url
        self.wait.until(EC.element_to_be_clickable(self.NAVIGATION_MENU)).click()
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        empty_input = self.driver.find_element(By.XPATH,
                                               "//div[contains(text(),'Enter your email or mobile phone number')]").text

        # print(ErrorMessage.please_enter_phone_or_email)

        self.driver.get(url)

        try:
            assert empty_input.lower() == ErrorMessage.please_enter_phone_or_email.lower()
        except AssertionError as e:
             allure.attach(self.driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)




    def login_with_invalid_email(self, email, expected):
        url = self.driver.current_url
        self.wait.until(EC.element_to_be_clickable(self.NAVIGATION_MENU)).click()
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        time.sleep(2)
        try:
            error_message = self.driver.find_element(By.XPATH,
                                                     "//h4[normalize-space()='There was a problem']").text.lower()
            if error_message:
                invalid_email_msg = self.driver.find_element(By.XPATH, "//span[@class='a-list-item']").text.lower()
                # print(invalid_email_msg)
                allure.attach(self.driver.get_screenshot_as_png(), name='failed_test',attachment_type=AttachmentType.PNG)
                assert invalid_email_msg == ErrorMessage.invalid_email_format.lower()
                # print(invalid_email_msg)
            # print(error_message)

        except NoSuchElementException as e:
            print(e)

        self.driver.get(url)

    def login_with_valid_username_but_invalid_password(self, username, password, expected):
        url = self.driver.current_url
        try:
            self.driver.find_element(*self.NAVIGATION_MENU).click()
            self.driver.find_element(*self.EMAIL_INPUT).clear()
            self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
            self.driver.find_element(*self.CONTINUE_BUTTON).click()
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
            self.driver.find_element(*self.SIGN_IN_BUTTON).click()
            incorrect_password_text = self.driver.find_element(By.XPATH, "//span[@class='a-list-item']").text.lower()
            assert incorrect_password_text == ErrorMessage.your_password_is_incorrect.lower()
        except NoSuchElementException as e:
            print("error")
            allure.attach(self.driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)


        time.sleep(3)
        self.driver.get(url)

    def login_with_valid_username_but_empty_password(self, username, password,expected):
        url = self.driver.current_url
        try:
            self.driver.find_element(*self.NAVIGATION_MENU).click()
            self.driver.find_element(*self.EMAIL_INPUT).clear()
            self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
            self.driver.find_element(*self.CONTINUE_BUTTON).click()
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
            self.driver.find_element(*self.SIGN_IN_BUTTON).click()
            error_message = self.driver.find_element(By.XPATH, "//div[contains(text(),'Enter your password')]").text
            assert error_message.lower() ==ErrorMessage.enter_your_password.lower();

        except NoSuchElementException as e:
            print("error")
            allure.attach(self.driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)
            pass

        time.sleep(3)
        self.driver.get(url)


    def login_with_valid_credentials(self, username, password, checkUserName):
        self.driver.find_element(*self.NAVIGATION_MENU).click()
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()
        time.sleep(10)
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
            allure.attach(self.driver.get_screenshot_as_png(), name='failed_test', attachment_type=AttachmentType.PNG)
            print(e)

    def validate_search_item(self, item_to_search, check_search):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(item_to_search)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        self.driver.find_element(By.XPATH,
                                 "//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'realme "
                                 "GT Neo 3 (Asphalt Black, 8GB RAM, 256GB Sto')]").click()

        time.sleep(2)
        current_url = self.driver.current_url
        try:
            assert current_url.lower().__contains__(check_search)
        except Exception as e:
             print(e)

        parentHandle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
