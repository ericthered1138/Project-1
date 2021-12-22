from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class EmployeePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def pom_enter_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementAmount")
        return element

    def pom_enter_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementReason")
        return element

    def pom_click_submit(self):
        element: WebElement = self.driver.find_element(By.ID, "create")
        return element

    def pom_grab_the_new_reimbursement(self, reason):
        element: WebElement = self.driver.find_element(By.ID, reason)
        return element
