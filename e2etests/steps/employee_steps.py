import time

from behave import Given as given, When as when, Then as then


@given(u'the employee is on the employee page')
def get_employee_page(context):
    # log into the employee page from the login page
    url = r"http://127.0.0.1:5500/website/login_page.html"
    context.driver.get(url)
    time.sleep(1)
    context.login_page.pom_enter_username().send_keys("passwordistaco")
    time.sleep(1)
    context.login_page.pom_enter_password().send_keys("taco")
    time.sleep(1)
    context.login_page.pom_click_login().click()


@when(u'the employee enters an amount')
def enter_amount(context):
    time.sleep(1)
    context.employee_page.pom_enter_amount().send_keys("24601")


@when(u'the employee enters a reason')
def enter_reason(context):
    time.sleep(1)
    context.employee_page.pom_enter_reason().send_keys("one day more")


@when(u'the employee clicks the submit button')
def click_submit(context):
    time.sleep(1)
    context.employee_page.pom_click_submit().click()


@then(u'a new reimbursement is added to the pending reimbursements table')
def grab_the_new_reimbursement(context):
    time.sleep(1)
    assert context.employee_page.pom_grab_the_new_reimbursement("one day more")


@when(u'the employee enters a negative amount')
def enter_negative(context):
    time.sleep(1)
    context.employee_page.pom_enter_amount().send_keys("-24601")


@then(u'an amount error pops')
def amount_error_check(context):
    time.sleep(1)
    assert context.driver.switch_to.alert.text == "Invalid Entry: Amounts must be positiver numbers."
    context.driver.switch_to.alert.accept()


@when(u'the employee enters a non_numeric amount')
def enter_non_numeric(context):
    time.sleep(1)
    context.employee_page.pom_enter_amount().send_keys("twofoursixohone")
