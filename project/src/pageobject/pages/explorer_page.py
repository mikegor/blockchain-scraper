from selenium.webdriver.common.by import By
from project.src.pageobject.locators import ExplorerPageLocator


class ExplorerPage:

    def __init__(self, driver):
        self.driver = driver
        self.all_blocks_button = driver.find_element(By.XPATH, ExplorerPageLocator.ALL_BLOCKS_BUTTON)

    def get_all_blocks_button(self):
        return self.all_blocks_button
