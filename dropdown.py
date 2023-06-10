# for dropdown --> the tagname is SELECT

import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drop_down = driver.find_element(By.XPATH,"//select[@id='country_name']")
# there is a select class from selenium for dropdowns,so import it
# so put select class inside object
drop_down_obj = Select(drop_down)
# inside select class there are  methods for dropdown
# this is to select the <option> web element inside <select tag>. options has many dropdown countries
drop_down_obj.select_by_visible_text("India")
drop_down_obj.select_by_value("5")
drop_down_obj.select_by_index(2) # manually count the dropdowns and give the index

# to find the total options , there is options variable.
all_options = drop_down_obj.options
print(len(all_options))

for opt in all_options:
    print(opt.text)

# how to select the dropdowns without using built in methods such as select_by_visible_text
for opt in all_options :
    if opt == "India":
        opt.click()
        break