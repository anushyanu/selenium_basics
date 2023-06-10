import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
#driver.get("http://automationpractice.pl/index.php")
driver.get("http://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)

#sliders : to find multiple web elements we use class name and tag name
# e.g inside li-> the class name for all li are same then use classname
#sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
#print(len(sliders))
#links = driver.find_elements(By.TAG_NAME,"a")
#print(len(links))

log = driver.find_element(By.XPATH , "//button[text()='Log in']")
print(log.text)





