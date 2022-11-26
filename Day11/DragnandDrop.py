
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
#source element
Oslo=driver.find_element(By.ID,"box1")
Stockholm=driver.find_element(By.ID,"box2")
Washington=driver.find_element(By.ID,"box3")
Copenhagen=driver.find_element(By.ID,"box4")
Seoul=driver.find_element(By.ID,"box5")
Rome=driver.find_element(By.ID,"box6")
Madrid=driver.find_element(By.ID,"box7")


#target element
Norway=driver.find_element(By.ID,"box101")
Sweden=driver.find_element(By.ID,"box102")
US=driver.find_element(By.ID,"box103")
Denmark=driver.find_element(By.ID,"box104")
South_Korea=driver.find_element(By.ID,"box105")
Italy=driver.find_element(By.ID,"box106")
Spain=driver.find_element(By.ID,"box107")


act=ActionChains(driver)
#drag and drop action
act.drag_and_drop(Rome,Italy).perform()
act.drag_and_drop(Seoul,South_Korea).perform()
act.drag_and_drop(Madrid,Spain).perform()
act.drag_and_drop(Washington,US).perform()
act.drag_and_drop(Oslo,Norway).perform()
act.drag_and_drop(Stockholm,Sweden).perform()
act.drag_and_drop(Copenhagen,Denmark).perform()

time.sleep(5)
driver.minimize_window()
time.sleep(1)
driver.quit()