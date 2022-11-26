
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--Disable Notifications--")

serv_obj=Service("C:\Drivers\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)


driver.get("https://whatmylocation.com/")

