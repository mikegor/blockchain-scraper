import unittest
import time

from project.src.scraperbase.web_driver_setup import WebDriverSetup
from project.src.pageobject.pages.google_home_page import GoogleHomePage

class GoogleSearch(WebDriverSetup):
    
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)

        home = GoogleHomePage(self.driver)
        time.sleep(1)
        agree = home.get_agree()
        agree.click()
        time.sleep(1)
        search_text = home.get_search_text()
        search_text.send_keys("testtest")
        time.sleep(1)
        search_text.submit()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()


