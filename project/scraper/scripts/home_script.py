import unittest
import time

from project.src.scraperbase.web_driver_setup import WebDriverSetup
from project.src.pageobject.pages.home_page import HomePage

class HomeScript(WebDriverSetup):

    def test_explorer_link(self):
        self.driver.get("https://www.blockchain.com/")
        self.driver.set_page_load_timeout(30)
        home = HomePage(self.driver)
        time.sleep(1)
        accept_cookies = home.get_accept_cookies()
        accept_cookies.click()
        time.sleep(1)
        explorer_link = home.get_explorer_link()
        explorer_link.click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()


