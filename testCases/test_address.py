import pytest

from base.base_driver import Message
from pages.address_page import AddressPage
from pages.amazon_home_page import AmazonHomePage


@pytest.mark.usefixtures("setup", "log_on_failure")
# @pytest.mark.order(3)
class TestAddress:
    def test_address_setup(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.amazon_current_url(Message.title)
        amazonHomePage.login_with_valid_credentials("9110164834","Shashi@123","shashi")

    @pytest.mark.parametrize("fullname, mobileNumber,pincode,flate_house,area, expected", [
        ("", "", "", "", "", "please fill the inputs"),
        (" ", "7073052300", "845305", "near bypass", "singhpu haraiya", "give enter ur name"),
        ("shashi kumar", "70730523", "845305", "near bypass", "singhpur haraiya", "invalid mobile number"),
        ("shashi kumar", "7073052300", "2101", "near bypass", "singhpur haraiya", "invalid pin code"),
        ("shashi kumar", "7073052300", "abc", "near bypass", "singhpur haraiya", "only integer is allowed"),
        ("shashi kumar", "7073052300", "845305", "near bypass", "", "please enter your address"),
        ("shashi kumar", "7073052300", "845305", "near bypass", "a", "address should be of 3 to 100 character"),
        ("shashi kumar", "7073052300", "845305", "", "singhpur haraiya raxaul", "please enter valid flate of house "
                                                                                "number"),
        ("shashi kumar", "7073052300", "845305", "3", "singhpur haraiya raxaul", "address already exist address"),

    ])
    def test_add_new_address_with_invalid_credentials(self, fullname, mobileNumber, pincode, flate_house, area, expected):
        addressPage = AddressPage(self.driver)
        addressPage.add_new_address_with_invalid_credentials(fullname, mobileNumber, pincode, flate_house, area, expected)

    def test_validate_adding_new_address_with_valid_credential(self):
        addressPage = AddressPage(self.driver)
        addressPage.validate_adding_new_address_with_valid_credential()