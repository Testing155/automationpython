from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
#driver.find_element(By.LINK_TEXT, "A/B Testing").c lick()

# partial linktext
driver.find_element(By.PARTIAL_LINK_TEXT,"A/B").click()