import os
from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://www.automationtesting.co.uk/calculator.html')
driver.implicitly_wait(5)

first_num = driver.find_element(By.ID, 'result')
symbol = driver.find_element(By.ID, 'result')
second_num = driver.find_element(By.ID, 'result')

first_num.send_keys(5)
symbol.send_keys("+")
second_num.send_keys(5)
