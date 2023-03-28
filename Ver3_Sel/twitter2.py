import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver
os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Twitter login page
driver.get("https://twitter.com/login")

# Wait for the page to load
driver.implicitly_wait(10)

# Find the email input field and enter the email address
email_field = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
email_field.send_keys("Student_21464553@outlook.com")
time.sleep(2)

# Click on the Next button
next_button = driver.find_element(By.XPATH, '//span[text()="Next"]')
next_button.click()

# Wait for the username or password input field to become clickable and enter the respective value
try:
    username_field = driver.find_element(By.NAME, 'text')
    username_field.send_keys('S2146455365372')
    time.sleep(2)
    next_button = driver.find_element(By.XPATH, '//span[text()="Next"]')
    next_button.click()
    time.sleep(2)
    
    # Wait for the password input field to become clickable and enter the password
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_field.send_keys('UWL2021!@')
    
except:
    try:
        # Wait for the password input field to become clickable and enter the password
        password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        password_field.send_keys('UWL2021!@')
        
    except:
        print("Could not find password field.")
    
# Click on the Log in button
login_button = driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
login_button.click()

# Wait for the login process to complete
time.sleep(2)

# Click on Profile
profile_button = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Profile"]')
profile_button.click()
time.sleep(2)

# Quit the browser
driver.quit()
