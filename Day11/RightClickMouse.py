
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo")

button=driver.find_element(By.XPATH,"//span[normalize-space()='right click me']")

act=ActionChains(driver)
act.context_click(button).perform() #right click

time.sleep(5)
driver.quit()