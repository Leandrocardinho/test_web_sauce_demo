# - Bibliotecas
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 2 - Classe e definições
class TestGoogle():
    def setup_method(self, method):
        #Instanciar o obj do Selenium webDriver como Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.vars = {}



    def teardown_method(self, method):
        self.driver.quit()

    def test_google_ide(self):
        self.driver.get("https://www.google.com.br")
        self.driver.set_window_size(1004, 708)
        time.sleep(5)  # Pausa por 5 segundos
        self.driver.find_element(By.XPATH ,"//*[@id='gb']/div/div[2]/a").click()
        self.driver.find_element(By.ID, "identifierId").send_keys("leandro_")
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button > span").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".J7pUA > .VfPpkd-vQzf8d").click()
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-ksKsZd-mWPk3d").click()
        self.driver.find_element(By.ID, "firstName").send_keys("leandro")
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys("japa")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-vQzf8d").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-vQzf8d")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

