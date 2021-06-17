from selenium.webdriver.common.by import By
from project.src.pageobject.locators import BlocksPageLocator


class BlocksPage:

    def __init__(self, driver):
        self.blocks_list = driver.find_elements(By.CLASS_NAME, BlocksPageLocator.BLOCK_CLASS)

    def get_blocks_list(self):
        return self.blocks_list

    def get_recent_blocks(self, block_list):
        recent_blocks = [block.find_element(By.CLASS_NAME, BlocksPageLocator.TIME_CLASS).text for block in block_list
                         if self.is_recent(block.find_element(By.CLASS_NAME, BlocksPageLocator.TIME_CLASS).text)]
        return recent_blocks

    def is_recent(self, added_time):
        splitted = added_time.split()
        if splitted[1] != 'minutes':
            return False
        elif splitted[1] == 'minutes':
            if int(splitted[0]) < 15:
                return True
            else:
                return False
