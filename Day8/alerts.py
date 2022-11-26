import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)
alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("welcome")

#alert_window.accept() #close alert window by using OK button
alert_window.dismiss() #close alert window by using Cancel button

