from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
driver.maximize_window()
driver.find_element(By.ID,"inputUsername").send_keys("abcd")
driver.find_element(By.NAME,"inputPassword").send_keys("abcd")
checkbox= driver.find_element(By.ID,"chkboxOne")
#CHECK IF NOT SELECTED
if not checkbox.is_selected():
    checkboxes =driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for checkbox in checkboxes:
        checkbox.send_keys(Keys.SPACE)
input()


