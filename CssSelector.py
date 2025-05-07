from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#implicit wait
driver.implicitly_wait(5)
    #prices
prices = driver.find_elements(By.CSS_SELECTOR,".inventory_item_price")

    #print all prices
for price in prices:
  print(price.text)
 

