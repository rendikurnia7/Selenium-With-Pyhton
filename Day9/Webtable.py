# 1) Count number of rows and columns
# 2) Read Specific row and column data
# 3) read all rows and column data
# 4) Read data based on condition(List books name whose author is Mukesh)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

# Count Number of Column

noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfCols=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noOfRows) #7
print(noOfCols) #4

# Read Specific row & column data

# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# Read ALL rows & columns
# print("Print All ros and column Data.............")
#
# for rows in range(2,noOfRows+1):
#     for cols in range(1,noOfCols+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rows)+"]/td["+str(cols)+"]").text
#         print(data,end='                      ')
#         print()



# 4) Read data based on condition(List books name whose author is Mukesh)
for rows in range(2,noOfRows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rows)+"]/td[2]").text
    if authorname=="Mukesh":
        bookName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rows)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rows)+"]/td[4]").text
        print(bookName,"        ",authorname,price)


driver.close()