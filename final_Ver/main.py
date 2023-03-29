import time
import os
from constant import BASE_URL, EMAIL, PASSWORD, USERNAME
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Twitter(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Twitter, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def load_page(self):
        self.get(BASE_URL)

        # Find the email input field and enter the email address
    def input_email(self):
        email_field = self.find_element(By.CLASS_NAME, 'r-30o5oe')
        email_field.send_keys(EMAIL)
        time.sleep(2)
        # Click on the Next button
        next_button = self.find_element(By.XPATH, '//span[text()="Next"]')
        next_button.click()

    def input_username(self):
        username_field = self.find_element(By.NAME, 'text')
        username_field.send_keys(USERNAME)
        time.sleep(2)
        next_button = self.find_element(By.XPATH, '//span[text()="Next"]')
        next_button.click()
        time.sleep(2)

    def input_password(self):
        try:
            username_field = self.find_element(By.NAME, 'text')
            username_field.send_keys('S2146455365372')
            time.sleep(2)
            next_button = self.find_element(By.XPATH, '//span[text()="Next"]')
            next_button.click()
            time.sleep(2)

            # Wait for the password input field to become clickable and enter the password
            password_field = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.NAME, 'password')))
            password_field.send_keys(PASSWORD)

        except NoSuchElementException:
            try:
                # Wait for the password input field to become clickable and enter the password
                password_field = WebDriverWait(self, 5).until(
                    EC.element_to_be_clickable((By.NAME, 'password')))
                password_field.send_keys('UWL2021!@')

            except:
                print("Could not find password field.")

    def button_login(self):
        login_button = self.find_element(
            By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        login_button.click()
        # Wait for the login process to complete
        time.sleep(2)

    def click_profile(self):
        # Click on Profile
        profile_button = self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="Profile"]')
        profile_button.click()
        time.sleep(2)

    def quit_driver(self):
        # Quit the browser
        self.quit()
