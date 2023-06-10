import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)


driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
time.sleep(5)
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

# to select multiple checkboxes
checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkbox))
#for box in checkbox:
    #box.click()


#time.sleep(10)

# multiple checkbox by choice
#for box in checkbox:
    #week = box.get_attribute('id')
    #if week == "monday" or week == "sunday":
     #   box.click()

 # clear the checkbox which is selected
for box in checkbox:
    box.click()

for box in checkbox:
    box.is_selected()
    box.click()
time.sleep(10)
