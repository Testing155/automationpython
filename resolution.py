from invokechrome import driver

driver.webdriver.chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.set_window_size(width= 768 , height =500)