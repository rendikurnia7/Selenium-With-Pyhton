import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#swicth frame method
#1) driver.switch_to.frame("name of frame")
#2) driver.switch_to.frame(id of frame)
#3) driver.switch_to.frame(webelement)
#4) driver.switch_to.frame(0)


driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content() #go back to main frame

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(3)
driver.switch_to.default_content() #go back to main frame

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()


#driver.maximize_window()



