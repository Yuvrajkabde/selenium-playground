from selenium import webdriver

from  selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



serv_obj=Service("C:\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://snapdeal.com/")

driver.maximize_window()
print(driver.page_source)
print(driver.title)
print("Hare krishna")
driver.close()

