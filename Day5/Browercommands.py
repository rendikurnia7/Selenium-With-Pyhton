import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.find_element(By.LINK_TEXT,"View News Archive").click()

time.sleep(5)

driver.close()