from selenium.webdriver.common.by import By
from project.src.pageobject.locators import HomePageLocator


class HomePage:

    def __init__(self, driver):
        self.explorer_link = driver.find_element(By.XPATH, HomePageLocator.EXPLORER_LINK)

    def get_explorer_link(self):
        return self.explorer_link
