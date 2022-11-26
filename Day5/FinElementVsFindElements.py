from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")


#1) Locator Matching with single web element
# element=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
# element.send_keys("Apple MacBook Pro 13-inch")
#
#2) Locator Matching with mutiple  web element
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text) #print first link from footer "sitemap"

#3) Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

#------  find_elements() - Return mutiple webElements
#1)Locator Matching With single web element
# elements=driver.find_elements(By.XPATH,'//*[@id="small-searchterms"]')
# print(len(elements)) #1
# elements[0].send_keys("Apple MacBook Pro 13-inch")

#2)Locator Matching With mutiple web element
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements)) #23
# #print(elements[0].text) #Sitemap
#
# for ele in elements:
#     print(ele.text)

#3) Element not available
elements=driver.find_elements(By.LINK_TEXT,"Log")
print(("Elements returned:",len(elements)))
