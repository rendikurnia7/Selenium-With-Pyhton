from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#id and element locators
'''
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
'''

#driver.find_element(By.CLASS_NAME,"ico-register").click()

driver.find_element(By.LINK_TEXT,"Wishlist").click()