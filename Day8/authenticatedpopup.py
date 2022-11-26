import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#driver.maximize_window()



