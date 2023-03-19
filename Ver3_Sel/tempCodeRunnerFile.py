import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 'r' convention for a prefix, role string specifying the PATH to different location
os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://www.automationtesting.co.uk/buttons.html")
# Better practice, to wait and load a web browser
driver.implicitly_wait(2)
find_element = driver.find_element(By.ID, 'btn_one')
find_element.click()  # Allow the click action to complete before the browser is closed
time.sleep(5)  # Wait for 5 seconds
driver.quit()
