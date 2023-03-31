import fold1.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    # Currency=None default value, not passing value all the time
    def change_currency(self, currency=None):
        currency_element = self.find_element(  # Assigning expression to a variable
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        selected_currency = self.find_element(
            By.XPATH, '//span[text()="Euro"]')
        selected_currency.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR, 'button[type=submit]')
        search_button.click()

    '''def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()'''

    # Context manager quit() ex - could give us lot more control to start and tear down things up
