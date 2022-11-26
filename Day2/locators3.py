from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://facebook.com")
# driver.maximize_window()

#CSS Selectors
'''
    1) tag id           tagname#valueofId       input#email 
    2) tag class        tagname#valueofClass    input.inputtext _55r1 _6luy
    3) tag attribute    tagname[attribute=value]    input[data-testid=royal_email]
    4) tag class attribute  tagname.valueofClass[attribute=value]    input.inputtext[data-testid=royal_email]
'''
#tag&id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("rendi_kurniawan28@yahoo.com")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("rendi_kurniawan28@yahoo.com")

#tag&class
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("rendi_kurniawan28@yahoo.com")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("rendi_kurniawan28@yahoo.com")

#tag&attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("rendi_kurniawan28@yahoo.com")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("rendi_kurniawan28@yahoo.com")

#tag class&attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("rendi_kurniawan28@yahoo.com")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("0215398408")
driver.find_element(By.NAME,"login").click()

