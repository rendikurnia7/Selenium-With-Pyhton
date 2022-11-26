from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")


#Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")     #Javascript Syntax
# value=driver.execute_script("return window,pageYOffset;")
# print("Number of Pixles moved: ",value)     #3000

#Scroll down until the element is visible
# flag=driver.find_element(By.XPATH,"//img[@alt='Flag of Indonesia']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window,pageYOffset;")
# print("Number of Pixles moved: ",value)     #5094


#Scroll Down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window,pageYOffset;")
print("Number of Pixles moved: ",value)     #6019

time.sleep(3)

#Scroll up to starting position
driver.execute_script("window.scrollBy(0,- document.body.scrollHeight)")
value=driver.execute_script("return window,pageYOffset;")
print("Number of Pixles moved: ",value)