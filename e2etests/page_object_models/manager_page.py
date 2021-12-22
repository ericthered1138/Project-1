from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ManagerPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def pom_manager_click_approve(self, reimbursement_id):
        element: WebElement = self.driver.find_element(By.ID, reimbursement_id)
        return element

    def pom_manager_click_submit(self):
        element: WebElement = self.driver.find_element(By.ID, "submitManagerReimbursementTable")
        return element

    def pom_grab_the_new_reimbursement(self, reason):
        element: WebElement = self.driver.find_element(By.ID, reason)
        return element

    def pom_check_to_see_stats(self):
        element: WebElement = self.driver.find_element(By.ID, "statisticsTable")
        return element

    def pom_grab_the_element(self, element_id):
        element: WebElement = self.driver.find_element(By.ID, element_id)
        return element
