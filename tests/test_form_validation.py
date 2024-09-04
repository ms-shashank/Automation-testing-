import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# tests/test_form_validation.py
import pytest
from utils.base_test import BaseTest
from selenium.webdriver.common.by import By

class TestFormValidation(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_form_submission(self):
        self.driver.get("https://www.saucedemo.com/")
        
        # Assuming there's a form to fill
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Verify error message
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Epic sadface" in error_message
