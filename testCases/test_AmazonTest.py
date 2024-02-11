import time

import pytest

from pages.address_page import AddressPage
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_page import AmazonSearchedPage


@pytest.mark.usefixtures("setup", "LogGen")
class TestAmazon:

    def test_amazon_title(self, LogGen):
        amazonHomePage = AmazonHomePage(self.driver)
        title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        url = "https://www.amazon.in/"
        amazonHomePage.amazon_current_url(title, url)

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

    #
    @pytest.mark.xfail
    def test_login_with_valid_credentials(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.login_with_valid_credentials("9110164834", "Shashi@123", "shashi")
        amazonHomePage.validate_search_item("realme gt neo 3 256GB", "realme")
        time.sleep(10)

    @pytest.mark.parametrize("fullname, mobileNumber,pincode,flate_house,area, expected", [
        ("", "", "", "", "", "please fill the inputs"),
        (" ", "7073052300", "845305", "near bypass", "singhpu haraiya", "give enter ur name"),
        ("shashi kumar", "70730523", "845305", "near bypass", "singhpur haraiya", "invalid mobile number"),
        ("shashi kumar", "7073052300", "2101", "near bypass", "singhpur haraiya", "invalid pin code"),
        ("shashi kumar", "7073052300", "abc", "near bypass", "singhpur haraiya", "only integer s allowed"),
        ("shashi kumar", "7073052300", "845305", "near bypass", "", "please enter your address"),
        ("shashi kumar", "7073052300", "845305", "near bypass", "a", "address should be of 3 to 100 character"),
        ("shashi kumar", "7073052300", "845305", "", "singhpur haraiya raxaul", "please enter valid flate of house "
                                                                                "number"),
        ("shashi kumar", "7073052300", "845305", "3", "singhpur haraiya raxaul", "address already exist address"),

    ])
    def test_add_new_address_with_invalid_credentials(self, fullname, mobileNumber, pincode, flate_house, area, expected):
        addressPage = AddressPage(self.driver)
        addressPage.add_new_address_with_invalid_credentials(fullname, mobileNumber, pincode, flate_house, area, expected);

    def test_validate_adding_new_address_with_valid_credential(self):
        addressPage=AddressPage(self.driver)
        addressPage.validate_adding_new_address_with_valid_credential()
