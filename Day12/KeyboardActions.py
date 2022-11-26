from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# CTRL+A
# CTRL+C
# TAB
# CTRL+V


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://text-compare.com/")

driver.maximize_window()
driver.implicitly_wait(10)

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")


input1.send_keys("Welcome to test automation")

act=ActionChains(driver)

#step 1 ---->CTRL+A Select all text
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#step 2 --->CTRL+C copy text
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#step 3 ----> press TAB

act.key_down(Keys.TAB).perform()

#step 4 ---> CTRL+V

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.minimize_window()
driver.quit()