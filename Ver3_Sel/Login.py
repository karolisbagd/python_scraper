import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://www.automationtesting.co.uk/calculator.html')
driver.implicitly_wait(5)

first_num = driver.find_element(By.ID, 'result')
symbol_add = driver.find_element(By.ID, 'result')
second_num = driver.find_element(By.ID, 'result')

first_num.send_keys(Keys.NUMPAD5)
time.sleep(2)
symbol_add.send_keys(Keys.ADD)
time.sleep(2)
second_num.send_keys(Keys.NUMPAD5)
time.sleep(2)

# Passing CSS expression
btn = driver.find_element(By.CSS_SELECTOR, 'input[onClick="solve()"]')
btn.click()
time.sleep(2)


# classes with spaces are refering to different classes
# CSS selector is pattern to filter an element by it's styling.
