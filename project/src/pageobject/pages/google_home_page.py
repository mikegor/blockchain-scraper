from selenium.webdriver.common.by import By
from project.src.pageobject.locators import Locator

class GoogleHomePage():
    def __init__(self, driver):
        self.driver = driver
        self.search_text = driver.find_element(By.XPATH, Locator.SEARCH_TEXT)
        self.submit = driver.find_element(By.XPATH, Locator.SUBMIT)

    def get_search_text(self):
        return self.search_text

    def get_submit(self):
        return self.submit