from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import os
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Drivers\chromedriver.exe")

    #Download file in desired location
    preferences={
        "download.default_directory:":location,"plugin.always_open_pdf_externally":True
    }
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="table-files"]/tbody/tr[1]/td[3]/a').click()

