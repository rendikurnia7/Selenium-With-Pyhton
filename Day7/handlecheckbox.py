import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

#1) Select Specific checkbox
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

#2) Select All Checkbox
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes)) #7

#Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click

#Approach 2
for checkbox in checkboxes:
     checkbox.click()

#3) Select Mutiple Checkbox by Choice
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         checkbox.click()


#4) Select last 3 Checkbox
#totalnumber of element -3 = 4
# for i in range(len(checkboxes)-3,len(checkboxes)): #range(4,7) --> 5,6,7
#     checkboxes[i].click()

#5) Select first 4 checkbox
# for i in range(len(checkboxes)):
#     if i<4:
#         checkboxes[i].click()

time.sleep(5)
#6) Clear all Checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()




#driver.quit()