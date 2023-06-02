import time  # Module for working with time
import os  # Module for interacting with the operating system
from Constant import TWITTER_URL, EMAIL, PASSWORD, TWITTER_USERNAME, FACEBOOK_URL  # Importing necessary constants from the Constant module
from selenium import webdriver  # Main module for web automation and testing tasks
from selenium.webdriver.support.wait import WebDriverWait  # Used for waiting a certain amount of time or until a condition is met
from selenium.webdriver.common.by import By  # Allows to refer to elements by different methods (ID, XPath, etc.)
from selenium.webdriver.support import expected_conditions as EC  # Allows creating certain conditions to wait for in WebDriverWait
from selenium.common.exceptions import NoSuchElementException  # Exception that is thrown when an element is not found
from selenium.webdriver.common.action_chains import ActionChains  # Allows to chain multiple actions together, like move and click


class SocialMedia(webdriver.Chrome):  # Define a class named SocialMedia that inherits from webdriver.Chrome
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):  # Initializer of the class, sets default path to the webdriver if not provided
        self.driver_path = driver_path  # Assign the provided driver path to self.driver_path
        os.environ['PATH'] += self.driver_path  # Add the webdriver's path to the system path
        super(SocialMedia, self).__init__()  # Call the initializer of the superclass (webdriver.Chrome)
        self.implicitly_wait(15)  # Make the driver wait implicitly for 15 seconds when trying to find any element not immediately available
        self.maximize_window()  # Maximizes the browser window
        
        self.html_file = None  # Initialize self.html_file as None
        
    def open_html_file(self, mode):  # Method to open an HTML file in a specified mode
        # Join the directory path of this script file with the file name "results.html"
        file_path = os.path.join(os.path.dirname(__file__), "results.html")
        try:  # Try to open the file
            self.html_file = open(file_path, mode, encoding='utf-8')  # Open the HTML file in the specified mode
        except IOError as e:  # If an IOError occurs
            print(f"Error opening file: {e}")  # Print the error message

        
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

    def twitter_input_password(self):  # Method to input Twitter password
        try:  # Try to find and interact with the username and password fields
            username_field = self.find_element(By.NAME, 'text')  # Find the username field
            username_field.send_keys(TWITTER_USERNAME)  # Input the Twitter username
            time.sleep(2)  # Pause for 2 seconds
            next_button = self.find_element(By.XPATH, '//span[text()="Next"]')  # Find the "Next" button
            next_button.click()  # Click the "Next" button
            time.sleep(2)  # Pause for 2 seconds
            # Wait until the password field is clickable and then find it
            password_field = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.NAME, 'password')))
            password_field.send_keys(PASSWORD)  # Input the password
        except NoSuchElementException:  # If a NoSuchElementException occurs
            try:  # Try to find the password field again
                # Wait until the password field is clickable and then find it
                password_field = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.NAME, 'password')))
                password_field.send_keys(PASSWORD)  # Input the password
            except:  # If any exception occurs
                print("Could not find password field.")  # Print an error message
                
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

    def tweet_results(self):  # Method to tweet results
        self.open_html_file("w")  # Open the HTML file in write mode

        self.write_to_html_file("<html>\n")
        self.write_to_html_file("<head>\n")
        self.write_to_html_file("</head>\n")
        self.write_to_html_file("<body>\n")
        self.write_to_html_file("<h1>Twitter Tweets</h1>\n")
        self.execute_script("window.scrollBy(0, 1000);")

        try:  # Try to find all tweet elements
            tweet_elements = WebDriverWait(self, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, ".//article[@data-testid='tweet']")))
        except Exception as e:  # If an Exception occurs
            print(f"No tweet elements found. Error: {e}")  # Print the error message
            self.end_html_file()  # Close the HTML file if no tweets are found
            return  # Exit the method

        for tweet_element in tweet_elements:  # For each tweet element
            try:  # Try to find the tweet text and time elements
                tweet_text_element = tweet_element.find_element(
                    By.XPATH, ".//div[@lang='en']").text
                time_element = tweet_element.find_element(
                    By.XPATH, ".//time").get_attribute("datetime")

                self.write_to_html_file("<p>Name: {}</p>\n".format(tweet_text_element))
                self.write_to_html_file("<p>Time: {}</p>\n".format(time_element.split('T')[0]))
                self.write_to_html_file("<hr>\n")
            except Exception as e:  # If an Exception occurs
                print(f"Error while processing tweet: {e}")  # Print the error message


        self.write_to_html_file("</body>\n") # Test are they making a difference, because started to write in HTML at the begining. 
        self.write_to_html_file("</html>\n")

        self.end_html_file()  # Close the HTML file after writing all the tweets


# Facebook

    def facebook_load_page(self):  # This method loads the Facebook page
        self.get(FACEBOOK_URL)  # It uses Selenium's get method to navigate to the URL defined as FACEBOOK_URL
        time.sleep(5)  # It then pauses for 5 seconds to let the page load

    def facebook_login_page(self):  # This method logs into the Facebook page
        try:  # It first tries to handle the cookies pop-up
            # It waits for the cookies decline button to be clickable, and then clicks it
            cookies_field = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Decline optional cookies']")))
            print("Cookies declined")  # It prints a success message
            cookies_field.click()  # It clicks the cookies decline button
            time.sleep(2)  # It pauses for 2 seconds
        except NoSuchElementException:  # If the cookies pop-up isn't found
            print("Cookies pop-up not found, moving on to the next step")  # It prints a message and proceeds to the next steps

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

    def facebook_click_profile(self):  # This method navigates to the Facebook profile
        # It first finds the account icon
        account_icon = self.find_element(By.XPATH, "//div[@class='x1rg5ohu x1n2onr6 x3ajldb x1ja2u2z']")
        account_icon.click()  # It clicks the account icon
        print("Account Clicked")  # It prints a success message
        time.sleep(2)  # It pauses for 2 seconds
        # It then finds the profile icon
        profile_icon = self.find_element(By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4']")
        profile_icon.click()  # It clicks the profile icon

    def scrape_posts(self):  # This method scrapes posts from the Facebook timeline
        self.open_html_file("a")  # It opens the HTML file in append mode
        # It writes a heading to the HTML file
        self.write_to_html_file("<h1>Facebook Posts</h1>\n")

        num_iterations = 5  # Number of scroll iterations
        scroll_increment = 400  # Scroll distance in pixels
        scroll_delay = 2  # Delay between each scroll iteration

        for _ in range(num_iterations):
            self.execute_script(f"window.scrollBy(0, {scroll_increment});")  # Scroll the page vertically
            time.sleep(scroll_delay)  # Pause between scrolls

        post_elements = self.find_elements(
            By.XPATH,
            ".//div[@class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']",  # XPath to locate post elements
        )

        print("Scraping posts from the timeline")
        time.sleep(2)  # Pause after scrolling

        print(f"Number of post elements: {len(post_elements)}")

        for post_element in post_elements:  # For each post element
        # It finds the post text element
            post_text_element = post_element.find_element(
                By.XPATH, ".//div[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs']"  # XPath to locate post text
            ).text

            self.implicitly_wait(5)
 
            time_element = post_element.find_element(
                By.XPATH, ".//span[@class='x1rg5ohu x6ikm8r x10wlt62 x16dsc37 xt0b8zv']"  # XPath to locate post time
            ).text
            self.implicitly_wait(5)

            self.write_to_html_file("<p>Name: {}</p>\n".format(post_text_element))  # It writes the post text to the HTML file
            self.write_to_html_file("<p>Time: {}</p>\n".format(time_element))  # It writes the post time to the HTML file
            self.write_to_html_file("<hr>\n")  # It adds a horizontal line to separate posts

        self.end_html_file()  # It closes the HTML file after writing all the posts
