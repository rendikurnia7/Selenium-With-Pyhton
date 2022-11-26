from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")

#Capture Cookies From browser
cookies=driver.get_cookies()
print("Size of Cookies:",len(cookies))

#print details all cookies

# for c in cookies:
#     #print(c)
#     print(c.get('name'),":",c.get('value'))


#Add new cookie to browser
driver.add_cookie({"name":"Mycookie","value":'1234'})
cookies=driver.get_cookies()
print("Size of Cookies After Adding new one:",len(cookies))

#Delete Spesific Cookie from the browser
driver.delete_cookie("Mycookie")
cookies=driver.get_cookies()
print("Size of Cookies After Deleting new one:",len(cookies))

#Delete All Cookie from the browser
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of Cookies After Deleting all:",len(cookies))
