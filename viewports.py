import time

from selenium import webdriver
Viewports =[(1024, 768), (412, 915), (540, 720)]
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")

try:
    for width, height in Viewports:
        driver.set_window_size(width, height)
        time.sleep(4)

finally:
    driver.close()
#driver.set_window_size(width= 1024, height=1366)
