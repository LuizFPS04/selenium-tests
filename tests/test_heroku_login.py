import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestHerokuLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testHerokuLoginSuccess(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/login")

        email_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys("tomsmith")
        password_input.send_keys("SuperSecretPassword!")

        btn_login = driver.find_element(By.CLASS_NAME, "radius")

        btn_login.click()

        time.sleep(2)

        message = driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", message)

    def testHerokuLoginFail(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/login")

        email_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys("username")
        password_input.send_keys("password")

        btn_login = driver.find_element(By.CLASS_NAME, "radius")

        btn_login.click()

        time.sleep(2)

        message = driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()