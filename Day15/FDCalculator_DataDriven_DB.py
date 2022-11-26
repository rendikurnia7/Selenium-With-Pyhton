from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import mysql.connector

serv_obj = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()
driver.implicitly_wait(10)

try:
    con = mysql.connector.connect(host='localhost'
                                  , user='root',
                                  passwd='',
                                  database='test')
    curs = con.cursor()  # create curosor
    curs.execute("select * from caldata")

    # Read Data from Database
    for row in curs:
        principle = row[0]
        rateofInterest = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_mvalue = row[5]

        # passing data to the aplication

        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofInterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrop = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrop.select_by_visible_text(per2)

        frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequencydrp.select_by_visible_text(freq)

        driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[1]/img').click()  # calculate button

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # validation
        if float(exp_mvalue) == float(act_mvalue):
            print("Passed")

        else:
            print("Test Failed")

        driver.find_element(By.XPATH, '//*[@id="fdMatVal"]/div[2]/a[2]').click()
        time.sleep(2)
    con.close()
except:
    print("Connection Failed")

driver.close()

