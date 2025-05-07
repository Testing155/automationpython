from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
drag = driver.find_element(By.ID, "column-a")
drop = driver.find_element(By.ID, "column-b")
actions = ActionChains(driver)

# Attempt to drag and drop (not effective on HTML5 dnd)
actions.drag_and_drop(drag, drop).perform()

# Pause and check
time.sleep(2)
