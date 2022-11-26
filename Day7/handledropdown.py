
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")

#Approach1
#dropcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
dropcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))


#select option from dropdown
dropcountry.select_by_visible_text("Indonesia")
#dropcountry.select_by_value("34")  #Burkina Faso
#dropcountry.select_by_index(22)     #belize #index start from 0 count like array

# capture all the country options and print them
all_options=dropcountry.options
print("Total Number of Options: ",len(all_options))
# for opt in all_options:
#     print(opt.text)


#Select option from dropdown without using built-in method
# for opt in all_options:
#     if  opt.text=="Indonesia":
#         opt.click()
#         break

#Approach2
all_optionss=driver.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(all_optionss))

#driver.quit()