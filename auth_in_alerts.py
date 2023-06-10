import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://the-internet.herokuapp.com/basic_auth")
# here there are two input box, so we cannot amke switch_to or send_keys. these will wor for only one input box.
# so below is the inject method inside the url itself to bypass the application
#driver.get("http://username:password@the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")



