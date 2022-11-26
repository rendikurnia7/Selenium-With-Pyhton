from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Drivers\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com")
print(driver.title)
print(driver.current_url)
driver.close()