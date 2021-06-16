from selenium.webdriver.common.by import By
from project.src.pageobject.locators import ExplorerPageLocator


class ExplorerPage:

    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies = driver.find_element(By.XPATH, ExplorerPageLocator.ACCEPT_COOKIES)
        self.all_blocks_button = driver.find_element(By.XPATH, ExplorerPageLocator.ALL_BLOCKS_BUTTON)

    def get_accept_cookies(self):
        return self.accept_cookies

    def get_all_blocks_button(self):
        return self.all_blocks_button

