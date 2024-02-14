import time

import pytest

from base.base_driver import Message
from fixtures.readExcelFile import get_data
from pages.address_page import AddressPage
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_page import AmazonSearchedPage


@pytest.mark.usefixtures("setup", "log_on_failure")

class TestAmazon:

    def test_amazon_title(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.amazon_current_url(Message.title)

    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password, expected",get_data())
    def test_readExcelFile(self, username,password,expected):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_invalid_phone_number(username, expected)

    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password, expected", [
        ("978784", "password1", "phone number should be of 10 digit"),
        ("7878882521122155", "password2", "phone number should be of 10 digit"),
        ("9110164878", "password3", "user is not register"),
        ("91101648xxx", "password3", "only numeric integer is allowed"),

    ])
    @pytest.mark.xfail
    def test_login_with_invalid_phone_number(self, username, password, expected):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_invalid_phone_number(username, expected)


    @pytest.mark.sanity
    def test_login_with_empty_input(self):

        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_empty_input(" ")


    @pytest.mark.parametrize("email, password, expected", [
        ("shashigmail.com", "password1", "invalid email"),
        ("Amit@.com", "password2", "invalid email"),
        ("shahsi123@gmail.com", "password3", "un register user"),
        ("91101648awshotmail", "password3", "invalid email"),
    ])

    def test_login_with_invalid_email(self, email, password, expected):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_invalid_email(email, expected)

    @pytest.mark.parametrize("username, password, expected", [
        ("9110164834", "a", "password must be of 3 to 15 numeric digit"),
        ("9110164834", "shashi@123", "password first Character must be capital"),
        ("9110164834", "Shashi123", "invalid password"),
    ])
    def test_login_with_valid_username_but_invalid_password(self, username, password, expected):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_valid_username_but_invalid_password(username, password, expected)

    def test_login_with_valid_username_but_empty_password(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_valid_username_but_empty_password("9110164834","","please enter valid password")


    def test_login_with_valid_credentials(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_valid_credentials("9110164834", "Shashi@123", "shashi")

