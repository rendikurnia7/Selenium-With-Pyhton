from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
#driver.maximize_window()
min_slider=driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider=driver.find_element(By.XPATH,"//body//div//span[2]")

print("Location before moving.............")
print(min_slider.location)      # {'x': 59, 'y': 250}
print(max_slider.location)      # {'x': 370, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,93,0).perform()
act.drag_and_drop_by_offset(max_slider,-92,0).perform()

print("Location after moving.............")
print(min_slider.location)      # {'x': 153, 'y': 250}

print(max_slider.location)      # {'x': 277, 'y': 250}

time.sleep(3)
driver.quit()