import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# driver.get("https://www.shopclues.com/")


def test_AmazonHomePage():
    driver.get("https://www.amazon.in/")
    assert driver.title=="Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert driver.current_url=="https://www.amazon.in/"



def test_validate_login():
    driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
    driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("9110164834")
    driver.find_element(By.XPATH,"//input[@id='continue']").click()
    driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("Shashi@123")
    driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
    text= driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").text
    print(text)
    assert text.lower().__contains__("shashi")
    try:
        assert text.lower().__contains__("vikash")
    except Exception as e:
        print(e)
def test_validate_searchItem():
    driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("realme gt neo 3 256GB")
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    driver.find_element(By.XPATH,"//span[normalize-space()='realme GT Neo 3 (Asphalt Black, 8GB RAM, 256GB Storage)']").click()
    print(driver.current_url)
    current_url = driver.current_url
    assert current_url.lower().__contains__("realme")
    parentHandle=driver.current_window_handle
    all_handles=driver.window_handles
    driver.switch_to.window(all_handles[-1])
    print(driver.current_url)
    try:
        dropDown = driver.find_element(By.XPATH, "//select[@id='quantity']")
    except:
        print("An exception occurred")

    # print(dropDown.is_displayed())
    if dropDown.is_displayed():
        dd=Select(dropDown)
        dd.select_by_value("2")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='buy-now-button']").click()
    # time.sleep(10)


def test_validate_paymet_page():
   checkout= driver.find_element(By.XPATH,"//h1[normalize-space()='Checkout']").text
   assert checkout.lower().__contains__("checkout")
   delivery_address= driver.find_element(By.XPATH,"//h3[@class='a-color-base clickable-heading expand-collapsed-panel-trigger']").text
   assert delivery_address.lower().__contains__("address")


