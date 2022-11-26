#install package "requests"
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")

all_links=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in all_links:
    url=link.get_attribute('href')
    try:
        response=requests.head(url)
    except:
        None

    if response.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url," is valid link")

print("Total number of broken links: ",count)