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
find_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
find_element.send_keys("Student_21464553@outlook.com")
time.sleep(2)
act_btn = driver.find_element(By.CSS_SELECTOR, 'div[class="css-1dbjc4n"]')
act_btn.click()
'''find_element = driver.find_element(By.CLASS_NAME, 'css-1dbjc4n')
find_element.send_keys("UWL2021!@")
find_element = driver.find_element(By.ID, 'submit')
find_element.click()'''
time.sleep(2) 
driver.quit()

#act_btn.click()
#find_element.send_keys("Student_21464553@uwl.ac.uk")
#find_element = driver.find_element(By.NAME, 'session[]')
#find_element.send_keys("")
#find_element = driver.find_element(By.XPATH, '//span[contains(text(),"Log in")]')
#find_element.click()  
#time.sleep(5)  # Wait for 5 seconds
#driver.quit()

#r-30o5oe