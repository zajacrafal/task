from browser import Browser
from pages.home_page import HomePage
from pages.login_page import LogInPage
from pages.registration_page import RegistrationPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LogInPage()
    context.registration_page = RegistrationPage()


def after_all(context):
    context.browser.close()