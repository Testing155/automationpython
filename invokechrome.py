import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
# to get title
title= driver.title
print(title)
time.sleep(3)
#to verify
#assert "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, abc" in title
driver.get("https://www.saucedemo.com/v1/checkout-step-one.html")
driver.back()
#time allocation
time.sleep(3)
#current url
current_url =driver.current_url
print(current_url)
input()
