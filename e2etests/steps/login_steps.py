import time

from behave import Given as given, When as when, Then as then


@given(u'the employee is on the login page')
def get_login_page(context):
    url = r"http://127.0.0.1:5500/website/login_page.html"
    context.driver.get(url)


@when(u'the employee enters their username in the username input box')
def enter_username(context):
    context.login_page.pom_enter_username().send_keys("passwordistaco")


@when(u'the employee enters their password in the password input box')
def enter_password(context):
    context.login_page.pom_enter_password().send_keys("taco")


@when(u'the employee clicks the login button')
def click_login(context):
    context.login_page.pom_click_login().click()


@then(u'the employee should be logged in and redirected to the employee home page')
def check_page_url(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee"


# for the manager
@given(u'the manager is on the login page')
def manager_get_login_page(context):
    url = r"http://127.0.0.1:5500/website/login_page.html"
    context.driver.get(url)


@when(u'the manager enters their username in the username input box')
def manager_enter_username(context):
    context.login_page.pom_enter_username().send_keys("KarlSagan888888")


@when(u'the manager enters their password in the password input box')
def manager_enter_password(context):
    context.login_page.pom_enter_password().send_keys("karlsaganrules")


@when(u'the manager clicks the login button')
def manager_click_login(context):
    context.login_page.pom_click_login().click()


@then(u'the manager should be logged in and redirected to the manager home page')
def manager_check_page_url(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Manager"


@when(u'the employee enters a faulty password')
def enter_bad_password(context):
    context.login_page.pom_enter_password().send_keys("password")


@then(u'a login error pops')
def error_pop_check(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Username or password entered incorrectly."
    context.driver.switch_to.alert.accept()
