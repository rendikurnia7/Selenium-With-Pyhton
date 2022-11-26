from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.foundit.in/")
driver.find_element(By.XPATH,'//div[@class="heroSection-buttonContainer_secondaryBtn__text"]').click()
driver.find_element(By.XPATH,'//*[@id="file-upload"]').send_keys("C:\\Users\\RezaRendi\\PycharmProjects\\pythonProject\\selenium\\Day12\\sample.pdf")