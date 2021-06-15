import unittest
from selenium import webdriver

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if(self.driver != None):
            print("Tearing down")
            self.driver.close()
            self.driver.quit()