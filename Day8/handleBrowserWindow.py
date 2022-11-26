from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
#Browser windows
#switch_to.window(WindowID)

#current_window_handle      ---->   Return windowID of Single Browser Window
#window_handles      ---->   Return windowID's of Multiple Browser Windows

#windowid=driver.current_window_handle
#print(windowid) #CDwindow-4133B2633942B76F50C69B7EC52E26F1  ----> every open new window diffrent windowID
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsID=driver.window_handles
#Approach1
# parentWindow=windowsID[0]
# childWindow=windowsID[1]
# #print(parentWindow,childWindow)
#
# driver.switch_to.window(childWindow)
# print(driver.title)
#
# driver.switch_to.window(parentWindow)
# print(driver.title)

#Approach2

# for winID in windowsID:
#     driver.switch_to.window(winID)
#     print(driver.title)

time.sleep(3)
for winID in windowsID:
    driver.switch_to.window(winID)
    if driver.title=="OrangeHRM":
        driver.close()
