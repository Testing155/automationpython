from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.quit()