import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 'r' convention for a prefix, role string specifying the PATH to different location
os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
# Better practice, to wait and load a web browser
driver.implicitly_wait(2)
find_element = driver.find_element(By.NAME, 'session[student_21464553@null.net]')
find_element.send_keys("your_username")
find_element = driver.find_element(By.NAME, 'session[]')
find_element.send_keys("your_password")
find_element = driver.find_element(By.XPATH, '//span[contains(text(),"Log in")]')
find_element.click()  
time.sleep(5)  # Wait for 5 seconds
driver.quit()