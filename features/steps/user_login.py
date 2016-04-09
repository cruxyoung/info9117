from behave import *
import re



@given("at the login screen")
def step_impl(context):
    context.browser.get(context.address + "/login")
    login_found = re.search("login", context.browser.page_source, re.IGNORECASE)
    assert login_found
    

@when("an existing user submits the correct {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)

@when("an existing user submits the correct {username} but incorrect {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)


@when("an unknown user submits some {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)
def submit_username_password(context, username, password):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    username_field.submit()
    context.response = context.browser.page_source


@then('the system should return "{text}" as the authentication status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response

    
