from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) #Second  #implicit wait


driver.get("https://google.com")
Search_box=driver.find_element(By.NAME,'q')
Search_box.send_keys("Selenium")
Search_box.submit()
#time.sleep(5) #not efective
driver.find_element(By.XPATH,'//h3[text()="Selenium"]').click()

