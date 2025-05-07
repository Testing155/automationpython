from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
time.sleep(3)
checkboxes = driver.find_elements(By.XPATH, "//div[@class='oxd-checkbox-wrapper']")
for box in checkboxes:
    time.sleep(2)
    box.click()





