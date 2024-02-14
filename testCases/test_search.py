import pytest

from base.base_driver import Message
from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_page import AmazonSearchedPage



@pytest.mark.usefixtures("setup", "log_on_failure")
class TestSearch:


    def test_search_setup(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.amazon_current_url(Message.title)
        amazonHomePage.login_with_valid_credentials("9110164834", "Shashi@123", "shashi")


    @pytest.mark.sanity
    def test_validating_search_item(self):
        amazonHomePage = AmazonHomePage(self.driver)
        amazonHomePage.validate_search_item("realme gt neo 3 256GB", "realme")


    def test_validating_payment_page(self):
        amazonSearchPage = AmazonSearchedPage(self.driver)
        amazonSearchPage.validate_selected_item()
        amazonSearchPage.validate_payment_page("checkout", "address")
