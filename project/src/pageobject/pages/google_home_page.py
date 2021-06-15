from selenium.webdriver.common.by import By
from project.src.pageobject.locators import Locator

class GoogleHomePage():
    def __init__(self, driver):
        self.driver = driver
        self.agree = driver.find_element(By.XPATH, Locator.AGREE)
        self.search_text = driver.find_element(By.XPATH, Locator.SEARCH_TEXT)

    def get_agree(self):
        return self.agree

    def get_search_text(self):
        return self.search_text