import time

from selenium import webdriver
driver = webdriver.Chrome()
viewports=[(1024,768),(375,667)]
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.set_window_size(width=360 , height=500)
try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(2)

finally:
    driver.close()