import time
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from data_driven_testing import xl_utils

ser_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(15)
#driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
#driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.get("https://www.moneycontrol.com/mccode/loginConsent.php?url=https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(50)
#https://www.moneycontrol.com/fixed-inescome/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true
driver.find_element(By.XPATH,//*[@id="ACCT_GPLUS_LOGIN"])

file ="/home/anushya/Documents/selenium_data_driven.xlsx"
rows = xl_utils.getRowCount(file,"Sheet1")
#https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true
for r in range(2, rows+1):
    princ = xl_utils.readData(file, "Sheet1", r, 1)
    rate =  xl_utils.readData(file, "Sheet1", r, 2)
    p1 =  xl_utils.readData(file, "Sheet1", r, 3)
    p2 = xl_utils.readData(file, "Sheet1", r, 4)
    freq = xl_utils.readData(file, "Sheet1", r, 5)
    exp_res = xl_utils.readData(file, "Sheet1", r, 6)

    # passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(p1)
    dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    dropdown.select_by_visible_text(p2)
    freqdropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    freqdropdown.select_by_visible_text(freq)
    driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    act_value=driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text
    if float(exp_res) == float(act_value):
        print("test passed")
        xl_utils.writeData(file,"Sheet",r,8,"passed")
        xl_utils.fillGreenColor(file,"Sheet",r,8)
    else:
        print("test failed")
        xl_utils.writeData(file, "Sheet", r, 8, "failed")
        xl_utils.fillRedColor(file, "Sheet", r, 8)
    driver.find_element(By.XPATH, "//img[@class='PL5']").click()
    time.sleep(2)




