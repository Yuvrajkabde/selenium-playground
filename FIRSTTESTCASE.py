
#All required Module for selenium
from sys import executable
import pytest
from selenium import webdriver
from  selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#Browser setup
serv_obj=Service("C:\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
#Navigate to LamdaTest selenium playground table
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
driver.implicitly_wait(30)
#Finding the no of entries present
table_rows= driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr")

# Locate search Box and search for "New York" entries
search_box = driver.find_element(By.XPATH,"//input[@type='search']")
search_box.send_keys("New York")
search_box.send_keys(Keys.RETURN)
#Wait for results to load (Used Implicit ,method)
driver.implicitly_wait(30)

#Calculate the no of rows

visible_row = driver.find_elements(By.XPATH,"//table/tbody/tr[@role='row']")

total_entries = len(table_rows)
visible_entries=len(visible_row)
print(visible_entries)
print(total_entries)


#Assertion
assert visible_entries ==5, f"Expected 5 entries, but got {visible_entries}"
assert total_entries ==24, f"Expected 24 entries, but got {total_entries}"

print("Search Validation Passed")

driver.close()



