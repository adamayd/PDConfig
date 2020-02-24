import os
import time
from selenium import webdriver

pdUrl = os.environ['PD_URL']
pdUser = os.environ['PD_USER']
pdPass = os.environ['PD_PASS']

driver = webdriver.Chrome()
driver.get(pdUrl)
userbox = driver.find_element_by_xpath('//*[@id="search"]')
userbox.send_keys(pdUser)

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

time.sleep(5)
driver.close()
