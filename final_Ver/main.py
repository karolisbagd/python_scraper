import time
import os
from constant import TWITTER_URL, EMAIL, PASSWORD, TWITTER_USERNAME, FACEBOOK_URL
from selenium import webdriver  # scroll down the website
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SocialMedia(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(SocialMedia, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def twitter_load_page(self):
        self.get(TWITTER_URL)

        # Find the email input field and enter the email address
    def twitter_input_email(self):
        email_field = self.find_element(By.CLASS_NAME, 'r-30o5oe')
        email_field.send_keys(EMAIL)
        time.sleep(2)
        # Click on the Next button
        next_button = self.find_element(By.XPATH, '//span[text()="Next"]')
        next_button.click()

    def twitter_input_password(self):
        try:
            username_field = self.find_element(By.NAME, 'text')
            username_field.send_keys(TWITTER_USERNAME)
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
                password_field.send_keys(PASSWORD)

            except:
                print("Could not find password field.")

    def twitter_button_login(self):
        login_button = self.find_element(
            By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        login_button.click()
        # Wait for the login process to complete
        time.sleep(2)

    def twitter_click_profile(self):
        # Click on Profile
        profile_button = self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="Profile"]')
        profile_button.click()
        time.sleep(2)

    def tweet_results(self):

        tweet_texts = []

        # Scroll down the webpage
        self.execute_script("window.scrollBy(0, 1000);")

        # Locate all the tweet elements on the page
        tweet_elements = self.find_elements(
            By.XPATH, ".//article[@data-testid='tweet']")

        if not tweet_elements:
            print("No tweet elements found.")

        for tweet_element in tweet_elements:
            try:
                tweet_text_element = tweet_element.find_element(
                    By.XPATH, ".//div[@data-testid='tweetText']").text
                time_element = tweet_element.find_element(
                    By.XPATH, ".//time[@datetime]").get_attribute("datetime")
                #datetime = time_element.get_attribute("datetime")
                tweet_texts.append(
                    {"Text": tweet_text_element, "Tweeted on": time_element.split('T')[0]})
            except Exception as e:
                print(f"Error: {e}")

        # Return the text of all the tweets
        return tweet_texts

    # Facebook

    def facebook_load_page(self):
        self.get(FACEBOOK_URL)
        time.sleep(10)


    def facebook_login_page(self):
        cookies_field = self.find_elements(By.XPATH, './/button[title="Only allow essential cookies"]')
        if len(cookies_field) > 0:
            cookies_field[0].click()
        try:
            email_field = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.ID, 'email')))
        except:
            print("Could not find email field.")
            return

        email_field.send_keys(EMAIL)
        time.sleep(2)

        try:
            password_field = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.NAME, 'password')))
        except:
            print("Could not find password field.")
            return

        password_field.send_keys(PASSWORD)