import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os




def chrome_setup(download_location):
    from selenium.webdriver.chrome.service import Service
    ser_obj = Service("/usr/local/bin/chromedriver")
    # to download the file in the desired location we use these 3 steps
    # os .getcwd is used for downlooading file in the specific place where you want.
    preferences = {"download.default_directory":download_location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=ser_obj, options=ops)
    return driver

location = os.getcwd()
mdriver = chrome_setup(location)
mdriver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
mdriver.maximize_window()
mdriver.find_element(By.XPATH, "//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file'])[1]").click()
time.sleep(5)
