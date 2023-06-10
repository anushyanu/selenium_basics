import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

# frames are used to navigate from one frame to other frame inside the application
# tage names such a frame , iframe ,form are all indicates the frame
# whenever you want to go to each frame you use driver.switch_to.frame(name,id,webelement)
# it cant go from directly from org.openqa.selenium link frame to webdriver link frame so we need to go back-
# to main page  and then go to webdriver link frame.

#syntax : switch_to.frame(name of the frame )
         # switch_to.frame(id of the frame)
         # switch_to.frame( web element of frame e.g <iframe>)
         # switch_to.frame(0) if only one frame then put 0 )


driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content() # this goes to main page


driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content() # this goes to main page


driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
# without switch_to.frame , this doesnt work because all are inside different frames in the application
# so use the frame in selenium 4
#switch_to.frame("id of the frame")
#switch_to.frame(" name of the frame")
#switch_to.frame("webelement such as frame")
#switch_to.frame("index")
