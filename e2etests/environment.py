from behave.runner import Context
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_models.login_page import LoginPage
from page_object_models.employee_page import EmployeePage
from page_object_models.manager_page import ManagerPage


def before_all(context: Context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.login_page = LoginPage(context.driver)
    context.employee_page = EmployeePage(context.driver)
    context.manager_page = ManagerPage(context.driver)
    context.driver.implicitly_wait(10)


def after_all(context):
    context.driver.quit()
