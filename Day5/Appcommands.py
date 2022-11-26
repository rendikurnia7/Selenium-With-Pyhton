from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title) #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source) #to capture source code of page


driver.quit()