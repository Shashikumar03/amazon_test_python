from datetime import time
from math import factorial

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# driver.get("https://www.shopclues.com/")
driver.get("https://www.amazon.in/")


print(driver.current_url)

driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("9110164834")
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("Shashi@123")
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
print("successfully login")
text= driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").text
print(text.lower().__contains__("shashi"))



