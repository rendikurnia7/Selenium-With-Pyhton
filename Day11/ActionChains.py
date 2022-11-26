from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
home=driver.find_element(By.XPATH,"//a[normalize-space()='Computers']")
dekstop=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']")


#Mouse hover
act=ActionChains(driver)
act.move_to_element(home).move_to_element(dekstop).click().perform()
time.sleep(2)


#dropdown option
custcurrency=Select(driver.find_element(By.XPATH,"//select[@id='customerCurrency']"))
custcurrency.select_by_visible_text("Euro")

driver.minimize_window()
#custcurrency.select_by_index(1)
#act.move_to_element(custcurrency).click().perform()