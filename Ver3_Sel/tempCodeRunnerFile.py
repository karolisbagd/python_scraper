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
symbol = driver.find_element(By.ID, 'result')
second_num = driver.find_element(By.ID, 'result')

first_num.send_keys(Keys.NUMPAD5)
time.sleep(2)
symbol.send_keys(Keys.ADD)
time.sleep(2)
second_num.send_keys(Keys.NUMPAD5)
time.sleep(2)


# classes with spaces are refering to different classes