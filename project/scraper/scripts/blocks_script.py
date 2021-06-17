import unittest
import time

from project.src.scraperbase.web_driver_setup import WebDriverSetup
from project.src.pageobject.pages.blocks_page import BlocksPage

class BlocksScript(WebDriverSetup):
    def test_get_blocks(self):
        time.sleep(1)
        blocks = BlocksPage(self.driver)
        blocks_list = blocks.get_blocks_list()
        recent_blocks = blocks.get_recent_blocks(blocks_list)
        print(recent_blocks)
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()