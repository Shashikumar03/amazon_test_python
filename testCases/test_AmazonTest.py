import time

import pytest

from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_page import AmazonSearchedPage


@pytest.mark.usefixtures("setup")
class TestAmazon:

    def test_amazon_title(self):
        amazonHomePage = AmazonHomePage(self.driver)
        title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
        url = "https://www.amazon.in/"
        amazonHomePage.amazon_current_url(title, url)
        amazonHomePage.validate_login("9110164834", "Shashi@123", "shashi")
        amazonHomePage.validate_search_item("realme gt neo 3 256GB", "realme")

    def test_validate_selected_item(self):
        amazonSearchedPage = AmazonSearchedPage(self.driver)
        amazonSearchedPage.validate_selected_item()
        amazonSearchedPage.validate_payment_page("checkout", "address")



