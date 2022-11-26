import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

#click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#Find Number of Links in page
#Links=driver.find_elements(By.TAG_NAME,'a')
Links=driver.find_elements(By.XPATH,'//a')
print("Total Number of Links: ",len(Links))

#print all of link names
for link in Links:
    print(link.text)