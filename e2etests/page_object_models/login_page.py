from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def pom_enter_username(self):
        element: WebElement = self.driver.find_element(By.ID, "username")
        return element

    def pom_enter_password(self):
        element: WebElement = self.driver.find_element(By.ID, "password")
        return element

    def pom_click_login(self):
        element: WebElement = self.driver.find_element(By.ID, "login")
        return element
