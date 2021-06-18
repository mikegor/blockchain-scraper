from unittest import TestLoader, TestSuite, TextTestRunner
from project.scraper.scripts.home_script import HomeScript
from project.scraper.scripts.explorer_script import ExplorerScript
from project.scraper.scripts.blocks_script import BlocksScript
from project.src.scraperbase.web_driver import WebDriver
from project.scraper.db.db import Db

if __name__ == "__main__":

    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(HomeScript),
        test_loader.loadTestsFromTestCase(ExplorerScript),
        test_loader.loadTestsFromTestCase(BlocksScript)
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    Db.insert_recent_blocks()

    WebDriver.web_driver_chrome.close()
    WebDriver.web_driver_chrome.quit()

