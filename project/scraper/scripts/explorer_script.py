import unittest
import time

from project.src.scraperbase.web_driver_setup import WebDriverSetup
from project.src.pageobject.pages.explorer_page import ExplorerPage

class ExplorerScript(WebDriverSetup):

    def test_view_all_blocks(self):
        explorer = ExplorerPage(self.driver)
        time.sleep(1)
        all_blocks_button = explorer.get_all_blocks_button()
        time.sleep(5)
        all_blocks_button.click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()