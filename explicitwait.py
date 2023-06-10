import time

from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception]) #this is explicit wait declaration.
# we should use exceptions in the declaration so if there is error in line22 then this exceptions shows and ggo to the
# next line.
# explicitwait works based on element not on time. so it includes multiple places if needed but declaration is needed only once.
#
driver.get("https://www.google.com/")
driver.maximize_window()

search = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("Selenium")
search.submit()
time.sleep(5)

searchlink = mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='Selenium']"))
# presence_of_element_located is used for locating the element using path and once it is found the until becomes
# ture and store in the search link.


searchlink.click()

driver.quit()