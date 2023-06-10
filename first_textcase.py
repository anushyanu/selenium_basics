# how to install chrome driver
# go to downloads in chrome and according to chrome version install the driver
# and extract it.then go to terminal go the folder where chromedriver is there.
# use command  sudo mv chromedriver /usr/local/bin
# use command export PATH=$PATH:/usr/local/bin/chromedriver
# now chrome driver works .


# TEST CASE

# open web browser(chrome/forefox/edge)
# open url https://opensource-demo.orangehrmlive.com/
# enter username( Admin)
# enter password (admin123)
# click login
# capture title of the home page(actual title)
# verify title of the page :orangehrm (expected)
# close the browser

# webdriver is a module which is available in selenium package
# chrome /firefox is a class inside webdriver so we create an object for chrome class


import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
# id and name locators
username = driver.find_element(By.NAME,"username")
username.send_keys("Admin")
userPwd = driver.find_element(By.NAME,"password")
userPwd.send_keys("admin123")

#driver.find_element(By.CSS_SELECTOR,".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
# also we can do using xpath
#driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(10)
act_tit = driver.title
exp_title = "OrangeHRM"
if act_tit == exp_title:
    print("login passed")
else:
    print("login failed")
driver.close()
#//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button







