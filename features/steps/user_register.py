from behave import *
import re

@given("at the register screen")
def step_impl(context):
    context.browser.get(context.address + "/register")
    register_found = re.search("Sign up", context.browser.page_source, re.IGNORECASE)
    assert register_found
    
    
@when("an new user submits the {username} and {password} and same {password2}")
def step_impl(context, username, password,password2):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    :type password2: str
    """
    submit_username_password_password2(context, username, password, password2)

@when("an new user submits the {username} and {password} and not same {password2}")
def step_impl(context, username, password,password2):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    :type password2: str
    """
    submit_username_password_password2(context, username, password, password2)

@when("an new user submits the same {username} and {password} and {password2}")
def step_impl(context, username, password,password2):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    :type password2: str
    """
    submit_username_password_password2(context, username, password, password2)



    
    

def submit_username_password_password2(context, username, password, password2):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    password2_field = context.browser.find_element_by_name("password2")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password2_field.send_keys(password2)
    username_field.submit()
    
    context.response = context.browser.page_source
    
@then('the system should return "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response
