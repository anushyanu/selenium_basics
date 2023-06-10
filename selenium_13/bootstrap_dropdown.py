import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)