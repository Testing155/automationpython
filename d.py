from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
dropdown = driver.find_element(By.ID, "dropdown")
dd = Select(dropdown)
dd.select_by_index(1)


 =