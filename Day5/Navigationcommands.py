from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://google.com")
driver.get("https://dropbox.com")

driver.back()
driver.forward()

driver.refresh()

driver.quit()