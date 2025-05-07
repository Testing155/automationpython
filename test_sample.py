import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    options = Options()
    # Run in headless mode (optional, can be removed for debugging)
    # options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_step_one(browser):

    browser.get("https://www.saucedemo.com/v1/index.html")

    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys("ABC")
    # driver.find_element(By.ID,"password").send_keys("test")
    # driver.find_element(By.ID, "login-button").click()
    # driver.find_element(By.)


