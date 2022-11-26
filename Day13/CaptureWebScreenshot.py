import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\RezaRendi\\PycharmProjects\\pythonProject\\Selenium with Pyton\\Day13\\homepage.png")
#driver.save_screenshot(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")



driver.quit()