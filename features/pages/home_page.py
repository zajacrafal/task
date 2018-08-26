from selenium.webdriver.common.by import By
from features.browser import Browser


class HomePageLoc(object):
    # Home Page Locators

    SUBMIT_BUTTON = (By.CLASS_NAME, 'global-header-section-button')


class HomePage(Browser):
    # Home Page Actions

    def click_element(self):
        self.driver.find_element(*HomePageLoc.SUBMIT_BUTTON).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title