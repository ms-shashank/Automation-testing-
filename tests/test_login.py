import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# tests/test_login.py
import pytest
from utils.base_test import BaseTest
from selenium.webdriver.common.by import By

class TestLogin(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Verify successful login
        assert "inventory.html" in self.driver.current_url

    @pytest.mark.usefixtures("setup")
    def test_invalid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Verify error message
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match" in error_message
