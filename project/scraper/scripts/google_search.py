import unittest
import time
from selenium import webdriver

from project.src.scraperbase.web_driver_setup import WebDriverSetup
from project.src.pageobject.pages.google_home_page import GoogleHomePage

class GoogleSearch(WebDriverSetup):
    
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)

        print('test')
        home = GoogleHomePage(self.driver)
        home.search_text.send_keys("testtest")
        time.sleep(5)
        home.search_text.submit()
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()


