from typing import Tuple

from selenium.webdriver.common.by import By
from browser import Browser


class Registration(object):
    # Registration Page Locators

    USER_NAME = (By.CSS_SELECTOR, '#name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    EMAIL = (By.CSS_SELECTOR, '#email')
    REGISTRATION_PAGE = (By.XPATH, '/html/body/div[1]/div[2]/a[2]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#signup')
    EMAIL_ERROR = (By.CSS_SELECTOR, '#email-error.error-message')
    EMAIL_ERROR_TAKEN = (By.CSS_SELECTOR, 'p.error-message')


class RegistrationPage(Browser):
    # Registration Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def fill_username(self, name):
        self.fill(name, *Registration.USER_NAME)

    def fill_correct_password(self, password):
        self.fill(password, *Registration.PASSWORD)

    def fill_wrong_password(self, password):
        self.fill(password, *Registration.PASSWORD)

    def fill_wrong_email(self, email):
        self.fill(email, *Registration.EMAIL)

    def fill_correct_email(self, email):
        self.fill(email, *Registration.EMAIL)

    def clear_email(self):
        self.driver.find_element(*Registration.EMAIL).clear()

    def register_page(self):
        self.driver.find_element(*Registration.REGISTRATION_PAGE).click()

    def registration_button(self):
        self.driver.find_element(*Registration.REGISTRATION_BUTTON).click()

    def get_register_page_title(self):
        return self.driver.title

    def email_error(self):
        self.driver.find_element(*Registration.EMAIL_ERROR).is_displayed()

    def email_taken(self):
        self.driver.find_element(*Registration.EMAIL_ERROR_TAKEN).is_displayed()

