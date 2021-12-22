import time

from behave import Given as given, When as when, Then as then


@when(u'the employee clicks the logout button')
def step_impl(context):
    context.employee_page.pom_grab_the_new_reimbursement("logout").click()


@then(u'the employee is on the login page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login"


@when(u'the manager clicks the logout button')
def step_impl(context):
    time.sleep(1)
    context.manager_page.pom_grab_the_element("logout").click()


@then(u'the manager is on the login page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Login"
