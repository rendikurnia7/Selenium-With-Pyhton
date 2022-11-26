from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
#driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countries_list=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countries_list))

for country in countries_list:
    if country.text=="Indonesia":
        country.click()
        break


