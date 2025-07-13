import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestGoogleDoodles(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def testGoogleDoodle(self):

        driver = self.driver
        driver.get("https://www.google.com")

        sorte_btn = driver.find_element(By.NAME, "btnI")
        print("Button found:", sorte_btn.get_attribute("value"))

        time.sleep(1)

        driver.execute_script("arguments[0].click();", sorte_btn)

        time.sleep(2)
        self.assertIn("Google Doodles", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()