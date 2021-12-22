import time

from behave import Given as given, When as when, Then as then


@then(u'the employee should see the past reimbursments table')
def step_impl(context):
    assert context.employee_page.pom_grab_the_new_reimbursement("oldReimbursementTable")


@then(u'the manager should see the pending reimbursement table')
def step_impl(context):
    assert context.manager_page.pom_grab_the_element("employeePendingReimbursementTable")


@then(u'the manager should see the past reimbursement table')
def step_impl(context):
    assert context.manager_page.pom_grab_the_element("employeeOldReimbursementTable")
