'''from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price").text()
input()'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait a bit to ensure the page loads properly (optional but good practice)
#driver.implicitly_wait(5)

# Get all the price elements
prices = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")

# Print each price
#for price in prices:
  #  print(price.text)

input()  # Keeps the window open until you press Enter
