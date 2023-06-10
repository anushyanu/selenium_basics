import time


from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# alerts doesnt have web elements

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# normalize-space() is also equal to text()
# webdriver provide switch_to.alert for  browser element to go to alert box, so we should make cursor to switch.

alert_window = driver.switch_to.alert # this represents the whole alert window
print(alert_window.text)
alert_window.send_keys("hello guys")
alert_window.accept() # this is to close the alert window using ok button
# alert_window.dismiss() is used to close alert window using cancel button
time.sleep(10)



