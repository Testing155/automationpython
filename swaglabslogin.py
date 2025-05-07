from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("ABC")
#driver.find_element(By.ID,"password").send_keys("test")
#driver.find_element(By.ID, "login-button").click()
#driver.find_element(By.)
input()
