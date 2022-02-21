import time

from behave import Given as given, When as when, Then as then


@given(u'the manager is on the manager page')
def manager_log_in(context):
    url = r"D:\MyDrive\Eric's Documents\0 Real Documents Folder\Revature\Project 1\Project-1\website\login_page.html"
    context.driver.get(url)
    context.login_page.pom_enter_username().send_keys("KarlSagan888888")
    context.login_page.pom_enter_password().send_keys("karlsaganrules")
    context.login_page.pom_click_login().click()


@when(u'the manager clicks the approve radio on one reimbursement')
def manager_click_approve(context):
    time.sleep(1)
    context.manager_page.pom_manager_click_approve("34567approval").click()


@when(u'the manager clicks the submit button on the table')
def manager_click_submit(context):
    time.sleep(1)
    context.manager_page.pom_manager_click_submit().click()


@then(u'one reimbursement is approved and sent to the previous reimbursements')
def grab_the_new_reimbursement(context):
    time.sleep(1)
    assert context.manager_page.pom_grab_the_new_reimbursement("a secret mission")


# for the disapproval
@when(u'the manager clicks the disapprove radio on one reimbursement')
def manager_click_disapprove(context):
    time.sleep(1)
    context.manager_page.pom_manager_click_approve("34568disapproval").click()


@when(u'the manager clicks the submit button')
def manager_click_submit(context):
    time.sleep(1)
    context.manager_page.pom_manager_click_submit().click()


@then(u'one reimbursement is disapproved and sent to the previous reimbursements')
def find_the_disapproved_reimbursement(context):
    time.sleep(1)
    assert context.manager_page.pom_grab_the_new_reimbursement("the secret of life")


@when(u'the manager inputs a comment in the one reimbursement comment box')
def manager_puts_in_comment(context):
    time.sleep(1)
    context.manager_page.pom_grab_the_element("34569comment").send_keys("and everything")


@when(u'the manager clicks the approve radio on the commented reimbursement')
def manager_clicks_on_comment_approve(context):
    time.sleep(1)
    context.manager_page.pom_manager_click_approve("34569approval").click()


@then(u'the commented reimbursement is approved and sent to the previous reimbursements')
def check_to_make_sure_the_comment_is_there(context):
    time.sleep(1)
    assert context.manager_page.pom_grab_the_new_reimbursement("the universe")
