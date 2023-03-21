import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 'r' convention for a prefix, role string specifying the PATH to different location
os.environ['PATH'] += r";C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://www.automationtesting.co.uk/buttons.html")

# Wait for the element to be clickable
find_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn_one')))
find_element.click()

# Wait for the alert to be present
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to alert and get text
text = alert.text

# Close the alert
alert.accept()

# Print the text
print(text)

# Quit the driver
driver.quit()
