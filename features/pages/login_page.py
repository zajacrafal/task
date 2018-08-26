from selenium.webdriver.common.by import By
from features.browser import Browser


class LogIn(object):
    # Search Results Page Locators

    USER_NAME = (By.CSS_SELECTOR, '#user')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login')


class LogInPage(Browser):
    # Search Results Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def fill_username(self, email):
        self.fill(email, *LogIn.USER_NAME)

    def fill_password(self, password):
        self.fill(password, *LogIn.PASSWORD)

    def login(self):
        self.driver.find_element(*LogIn.LOGIN_BUTTON).click()

    def get_login_page_title(self):
        return self.driver.title