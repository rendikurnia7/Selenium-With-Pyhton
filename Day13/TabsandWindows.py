
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#Just Open Link in New tab
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# regilink=Keys.CONTROL+Keys.RETURN  #New Tab Action
# driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)


# Open new Tab and Switch to new tab

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://demo.nopcommerce.com/")

# Open new Tab and Window to new Window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/")