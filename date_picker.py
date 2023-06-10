import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
time.sleep(1)

year = "2024"
date = "10"
month = "January"

while True:
    mon = driver.find_element(By.XPATH,"//*[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//*[@class ='ui-datepicker-year']").text
    if mon == month and yr == year:
        break;
    else:
        driver.find_element(By.XPATH,"/html/body/div/div/a[2]/span").click()

# select date now
dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break;

time.sleep(7)
