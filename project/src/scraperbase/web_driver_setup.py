import unittest
from project.src.scraperbase.web_driver import WebDriver

class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver.web_driver_chrome
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if(self.driver != None):
            print("Tearing down")
