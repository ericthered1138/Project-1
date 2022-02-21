import time

from behave import Given as given, When as when, Then as then


@given(u'the manager is on their page')
def get_to_the_manager_page(context):
    url = r"D:\MyDrive\Eric's Documents\0 Real Documents Folder\Revature\Project 1\Project-1\website\login_page.html"
    context.driver.get(url)
    context.login_page.pom_enter_username().send_keys("KarlSagan888888")
    context.login_page.pom_enter_password().send_keys("karlsaganrules")
    context.login_page.pom_click_login().click()


@then(u'the manager can see employee stats')
def check_to_see_stats(context):
    time.sleep(1)
    assert context.manager_page.pom_check_to_see_stats()
