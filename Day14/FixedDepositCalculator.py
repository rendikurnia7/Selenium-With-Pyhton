from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import XLUtils


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

driver.find_element(By.XPATH,'//*[@id="wzrk-cancel"]').click()
driver.implicitly_wait(10)

file="C:\\Users\\RezaRendi\\PycharmProjects\\pythonProject\\selenium\\Day14\\Test1.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    principle=XLUtils.readData(file,"Sheet1",r,1)
    rateofInterest=XLUtils.readData(file,"Sheet1",r,2)
    per1=XLUtils.readData(file,"Sheet1",r,3)
    per2=XLUtils.readData(file,"Sheet1",r,4)
    freq=XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue=XLUtils.readData(file,"Sheet1",r,6)

    #passing data to the aplication

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

    perioddrop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrop.select_by_visible_text(per2)

    frequencydrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(freq)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img').click() #calculate button

    act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(exp_mvalue)==float(act_mvalue):
        print("Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUtils.writeData(file,"Sheet1",r,8,"Failed")
        XLUtils.fillRedColor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]').click()
