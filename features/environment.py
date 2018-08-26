from features.browser import Browser
from features.pages.home_page import HomePage
from features.pages.login_page import LogInPage
from features.pages.registration_page import RegistrationPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = LogInPage()
    context.registration_page = RegistrationPage()


def after_all(context):
    context.browser.close()