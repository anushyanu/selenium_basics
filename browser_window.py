#in browser --> if you open the url the browser is always focused of the first url.
# driver.close() makes the first tab/window to get closed
# driver.quit() makes all the tabs/window  which are opened to get closed immediately
# if you open the first url and then you go to some link , this opens in next tab. so browseralways focused on the first tab
# so we need to switch from one tab to other. you can see below commands

import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

# when you open the tab it gives the window id and  close it, if you open again the same url again it gives different id.
# to get current window id use below
# current_window = driver.current_window_handle
#print(current_window)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# to get multiple window ids then use below one
multiple_ids = driver.window_handles

# all the ids are stored in a list to access -> use index.
parent_window_id = multiple_ids[0]
child_window_id = multiple_ids[1]
print(parent_window_id,child_window_id) #CDwindow-272A1454561FC690FE946064DBCFB6A6 CDwindow-1CF70F203F7539E49D7E71A054706077

# now we have ids of each window so can switch from one to other
driver.switch_to.window(child_window_id)
print("child : ", driver.title)

driver.switch_to.window(parent_window_id)
print("parent : ", driver.title)

# approach 2 : if you have more than 10 windows then use loop
for win_id in multiple_ids:
    driver.switch_to.window(win_id)
    print(driver.title)

# if you want to close the tab as per your choice then below is the code
for win_id in multiple_ids :
    driver.switch_to.window(win_id)
    if driver.title == "OrangeHRM":
        driver.close()












