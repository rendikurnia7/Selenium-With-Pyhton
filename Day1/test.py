#Test Case

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


'''
#facebook
driver.get("https://www.facebook.com/")

driver.find_element(By.NAME,"email").send_keys("rendi_kurniawan28@yahoo.com")
driver.find_element(By.ID,"pass").send_keys("0215398408")
driver.find_element(By.NAME,"login").click()
'''

'''
driver.get("https://dropbox.com/login")

driver.find_element(By.NAME,"login_email").clear()
driver.find_element(By.NAME,"login_email").send_keys("rendibm2@gmail.com")
driver.find_element(By.NAME,"login_password").clear()
driver.find_element(By.NAME,"login_password").send_keys("0215398408")
driver.find_element(By.CLASS_NAME,"signin-text").click()
'''

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()


