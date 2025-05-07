import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
dropdown =driver.find_element(By.ID, "dropdown")
#whose tagname is select
dd = Select(dropdown)
#dd.select_by_index(2)
time.sleep(2)
#dd.select_by_value("1")
dd.select_by_visible_text("Option 2")