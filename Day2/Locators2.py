from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://automationpractice.com/index.php")
# driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #5 total numbers of sliders on homepage

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #149 total numbers of link on homepage

driver.close()