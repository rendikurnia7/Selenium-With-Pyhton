from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#self

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Engineers India')]/self::a").text
# print(text_msg) #engineers India

#parent

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Engineers India')]/parent::td").text
# print(text_msg) #engineers India

# child
# chlds=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/child::td")
# print(len(childs)) #5

#ancestor
# ancestor=driver.find_element(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr").text
# print(ancestor) #all element row

#descendant
#descendant=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/descendant::*")
#print("Number of descendant nodes:",len(descendant)) #7

#following
#following=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/following::*")
#print("Number of following nodes:",len(following)) #3095

#following-Sibling
#following_sibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/following-sibling::*")
#print("Number of descendant following-siblings:",len(following_sibling)) #369


#preceding
#preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/preceding::*")
#print("Number of descendant preceding:",len(preceding)) #370

#preceding-sibling
preceding_sibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Engineers India')]/ancestor::tr/preceding-sibling::*")
print("Number of descendant preceding:",len(preceding_sibling)) #27





driver.close()