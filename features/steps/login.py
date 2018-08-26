from behave import *
from nose.tools import assert_equal
import time


@given('The trello.com is opened')
def step_impl(context):
    context.home_page.navigate('https://trello.com')
    assert_equal(context.home_page.get_page_title(), 'Trello')


@step('The login page is opened')
def step_impl(context):
    context.home_page.click_element()
    assert_equal(context.home_page.get_page_title(), 'Zaloguj do Trello')


@when('In login form email "{email}" and password "{password}" are entered')
def step_impl(context, email, password):
    context.login_page.fill_username(email)
    context.login_page.fill_password(password)
    context.login_page.login()
    time.sleep(10)


@then('User is logged in')
def step_impl(context):
    assert_equal(context.login_page.get_login_page_title(), 'Tablice | Trello')