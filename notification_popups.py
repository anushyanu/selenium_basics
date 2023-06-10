import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions() # this is a browser level.
ops.add_argument("--disable-notifications")

ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj,options = ops)


driver.get("https://whatmylocation.com/")
driver.maximize_window()