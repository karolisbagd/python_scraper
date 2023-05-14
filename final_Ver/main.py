import time
import os
from constant import TWITTER_URL, EMAIL, PASSWORD, TWITTER_USERNAME, FACEBOOK_URL
from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class SocialMedia(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(SocialMedia, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        self.html_file = None
        
    def open_html_file(self, mode):
        file_path = os.path.join(os.path.dirname(__file__), "results.html")
        try:
            self.html_file = open(file_path, mode, encoding='utf-8')
        except IOError as e:
            print(f"Error opening file: {e}")

        
    def write_to_html_file(self, content):
        if self.html_file is not None:
            try:
                self.html_file.write(content)
            except Exception as e:
                print(f"Error writing to file: {e}")
                
    def end_html_file(self):
        if self.html_file is not None:
            self.html_file.close()
            self.html_file = None  # Reset to None after closing

    def twitter_load_page(self):
        self.get(TWITTER_URL)

    def twitter_input_email(self):
        email_field = self.find_element(By.CLASS_NAME, 'r-30o5oe')
        email_field.send_keys(EMAIL)
        time.sleep(2)
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
            password_field = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.NAME, 'password')))
            password_field.send_keys(PASSWORD)
        except NoSuchElementException:
            try:
                password_field = WebDriverWait(self, 5).until(
                    EC.element_to_be_clickable((By.NAME, 'password')))
                password_field.send_keys(PASSWORD)
            except:
                print("Could not find password field.")

    def twitter_button_login(self):
        login_button = self.find_element(
            By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        login_button.click()
        time.sleep(2)

    def twitter_click_profile(self):
        profile_button = self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="Profile"]')
        profile_button.click()
        time.sleep(2)

    def tweet_results(self):
        self.open_html_file("w")  # Open the HTML file in write mode

        self.write_to_html_file("<html>\n")
        self.write_to_html_file("<head>\n")
        self.write_to_html_file("</head>\n")
        self.write_to_html_file("<body>\n")
        self.write_to_html_file("<h1>Twitter Tweets</h1>\n")
        self.execute_script("window.scrollBy(0, 1000);")

        try:
            tweet_elements = WebDriverWait(self, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, ".//article[@data-testid='tweet']")))
        except Exception as e:
            print(f"No tweet elements found. Error: {e}")
            self.end_html_file()  # Close the HTML file if no tweets are found
            return

        for tweet_element in tweet_elements:
            try:
                tweet_text_element = tweet_element.find_element(
                    By.XPATH, ".//div[@lang='en']").text
                time_element = tweet_element.find_element(
                    By.XPATH, ".//time").get_attribute("datetime")

                self.write_to_html_file("<p>Name: {}</p>\n".format(tweet_text_element))
                self.write_to_html_file("<p>Time: {}</p>\n".format(time_element.split('T')[0]))
                self.write_to_html_file("<hr>\n")
            except Exception as e:
                print(f"Error while processing tweet: {e}")

        self.write_to_html_file("</body>\n")
        self.write_to_html_file("</html>\n")

        self.end_html_file()  # Close the HTML file after writing all the tweets







   #{"Text": tweet_text_element, "Tweeted on": time_element.split('T')[0]})



# Facebook

    def facebook_load_page(self):
        self.get(FACEBOOK_URL)
        time.sleep(5)

    def facebook_login_page(self):
        try:
            cookies_field = WebDriverWait(self, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='Decline optional cookies']")))
            print("Cookies declined")
            cookies_field.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Cookies pop-up not found, moving on to the next step")

        email_field = self.find_element(By.NAME, 'email')
        print("Email entered")
        email_field.click()
        email_field.send_keys(EMAIL)
        time.sleep(2)

        password_field = self.find_element(By.NAME, 'pass')
        print("Password entered")
        password_field.click()
        password_field.send_keys(PASSWORD)
        time.sleep(2)
        login_button = self.find_element(By.NAME, 'login')
        login_button.click()
        print("Logging in... Please wait")
        time.sleep(8)

        actions = ActionChains(self)

        # Perform the click action
        actions.click().perform()
        time.sleep(2)

    def facebook_click_profile(self):
        account_icon = self.find_element(
            By.XPATH, "//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']")
        account_icon.click()
        print("Account Clicked")
        time.sleep(2)
        profile_icon = self.find_element(By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4']")
        profile_icon.click()

    def scrape_posts(self):
        self.open_html_file("a")  # Open the HTML file in append mode
        self.write_to_html_file("<h1>Facebook Posts</h1>\n")

        
        # Scroll down the webpage
        self.execute_script("window.scrollBy(0, 20000);")
        self.implicitly_wait(5)

        # Locate all the post elements on the page
        post_elements = self.find_elements(
            By.XPATH, ".//div[@class='x9f619 x1n2onr6 x1ja2u2z xeuugli xs83m0k x1xmf6yo x1emribx x1e56ztr x1i64zmx xjl7jj x19h7ccj xu9j1y6 x7ep2pv']")

        print("Scraping posts from the timeline")
        time.sleep(2)

        print(f"Number of post elements: {len(post_elements)}")

        for post_element in post_elements:
            post_text_element = post_element.find_element(
                By.XPATH, ".//div[@class='x1swvt13 x1pi30zi xexx8yu x18d9i69']").text # This works as well x1swvt13 x1pi30zi xexx8yu x18d9i69, xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs
            self.implicitly_wait(5)

            time_element = post_element.find_element(
                By.XPATH, ".//div[@class='xu06os2 x1ok221b']").text
            self.implicitly_wait(5)

            self.write_to_html_file("<p>Name: {}</p>\n".format(post_text_element))
            self.write_to_html_file("<p>Time: {}</p>\n".format(time_element))
            self.write_to_html_file("<hr>\n")

        self.end_html_file()  # Close the HTML file after writing all the posts
