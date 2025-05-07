import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
driver.maximize_window()
driver.find_element(By.ID,"inputUsername").send_keys("ABC")
driver.find_element(By.NAME,"inputPassword").send_keys("1234")
checkbox = driver.find_element(By.ID, "chkboxOne")
if not checkbox.is_selected():
  checkbox.click()

  time.sleep(2)
  if checkbox.is_selected():
      checkbox.click()
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

          # Click each checkbox if not already selected
for checkbox in checkboxes:
 checkbox.send_keys(Keys.SPACE)
