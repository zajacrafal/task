from behave import *
from nose.tools import assert_equal, assert_true


@given('The trello.com registration page is opened')
def step_impl(context):
    context.home_page.navigate('https://trello.com')
    context.registration_page.register_page()
    assert_equal(context.registration_page.get_register_page_title(), 'Stwórz konto Trello')


@step('In registration form name "{name}" and wrong password "{password}" are entered')
def step_impl(context, name, password):
    context.registration_page.fill_username(name)
    context.registration_page.fill_wrong_password(password)


@when('Wrong email structure "{wrong_email}" is entered')
def step_impl(context, wrong_email):
    context.registration_page.fill_wrong_email(wrong_email)


@then('Wrong email address error is occurred')
def step_impl(context):
    assert_true(context.registration_page.email_error)


@step('Email is corrected to "{correct_email}"')
def step_impl(context, correct_email):
    context.registration_page.clear_email()
    context.registration_page.fill_correct_email(correct_email)
    context.registration_page.registration_button()


@step('Password is corrected to "{correct_password}"')
def step_impl(context, correct_password):
    context.registration_page.fill_correct_password(correct_password)


@step("Error is occurred that email is already taken")
def step_impl(context):
    context.registration_page.registration_button()
    assert_true(context.registration_page.email_taken)