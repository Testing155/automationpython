from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("ABS")
driver.find_element(By.ID,"password").send_keys("456")
driver.find_element(By.ID,"login-button").click()
# Wait until you press Enter
input()
