from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")

#is_displayed is_enable
'''search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status:",search_box.is_displayed()) #true
print("Display Status:",search_box.is_enabled())  #true
'''

#is_selected for radio and check box

rd_male=driver.find_element(By.XPATH,'//*[@id="gender-male"]')
rd_female=driver.find_element(By.XPATH,'//*[@id="gender-female"]')

print(rd_male.is_selected())    #false
rd_male.click()
print("After Selected male....",rd_male.is_selected())

print(rd_female.is_selected())  #false

driver.quit()

