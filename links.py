# internal links
# external links
# broken links
# install the requests from settings ->project interpreter -> + -> requests
#

import time
import requests
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://deadlinkcity.com/") # this goes the server using requests and we can access through status code
# if it is above 400 then it is a broken link.
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,'a')
count = 0
for link in all_links:
    url = link.get_attribute('href')
    # try and except is used for requests to the server ( mostly api)
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, "is a broken link")
        count += 1
    else:
        print(url, "is a valid link")

print("total links", count)

time.sleep(5)


