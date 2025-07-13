import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestHerokuLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testMenuEnsinoLink(self):
        driver = self.driver
        driver.get("https://ifmg.edu.br/sabara")

        education_menu = driver.find_element(By.LINK_TEXT, "Ensino")
        education_menu.click()

        time.sleep(2)

        self.assertIn("Ensino", driver.title)

    def testMenuExtensaoLink(self):
        driver = self.driver
        driver.get("https://ifmg.edu.br/sabara")

        extension_menu = driver.find_element(By.LINK_TEXT, "Extensão")
        extension_menu.click()

        time.sleep(2)

        self.assertIn("Coordenação de Extensão e Relações Institucionais", driver.title)

    def testBusca(self):
        driver = self.driver
        driver.get("https://ifmg.edu.br/sabara")

        search = driver.find_element(By.NAME, "SearchableText")
        search.send_keys("edital")
        search.send_keys(Keys.ENTER)
        
        time.sleep(2)

        results = driver.find_element(By.ID, "content-core")
        self.assertTrue("resultado" in results.text.lower() or results.is_displayed())

if __name__ == "__main__":
    unittest.main()