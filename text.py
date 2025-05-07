from selenium import webdriver
from selenium.webdriver.common.by import By


# Set up Chrome browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://the-internet.herokuapp.com/")


# Click the link using link text
driver.find_element(By.LINK_TEXT, "A/B Testing").click()

# Use partial link text to find and click the link
driver.find_element(By.PARTIAL_LINK_TEXT, "Testing").click()





