from selenium.webdriver.common.by import By
from project.src.pageobject.locators import BlocksPageLocator
from datetime import datetime

class DataToSave:

    blocks = ()

    @staticmethod
    def set_blocks(blocks_to_set):
        DataToSave.blocks = blocks_to_set

    @staticmethod
    def get_blocks():
        blocks_to_get = [(DataToSave.get_height(block), DataToSave.get_hash(block),
                          DataToSave.get_date(), DataToSave.get_size(block))
                         for block in DataToSave.blocks]
        return blocks_to_get

    @staticmethod
    def get_height(block):
        return int(block.find_element(By.CLASS_NAME, BlocksPageLocator.HEiGHT_CLASS).text)

    @staticmethod
    def get_hash(block):
        return block.find_element(By.CLASS_NAME, BlocksPageLocator.HASH_CLASS).text

    #to do create proper date based on added time
    @staticmethod
    def get_date():
        current_date = datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date

    @staticmethod
    def get_size(block):
        return block.find_element(By.CLASS_NAME, BlocksPageLocator.SIZE_CLASS).text