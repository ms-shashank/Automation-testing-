import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# tests/test_ui.py
import pytest
from utils.base_test import BaseTest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestUI(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_homepage_ui_elements(self):
        self.driver.get("https://www.saucedemo.com/")
        
        # Login
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.RETURN)
        
        # Verify successful login
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html")
        )
        
        # Wait for the product to be clickable and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        ).click()
        
        # Wait for the add to cart button and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        ).click()
        
        # Verify the product item is displayed
        product_item = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_container"))
        )
        assert product_item.is_displayed(), "Product item is not displayed after login and selection"

        # Verify the navigation menu button is displayed
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
        )
        assert menu_button.is_displayed(), "Menu button is not displayed after login"
        
        # Verify the footer is displayed
        footer = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footer_copy"))
        )
        assert footer.is_displayed(), "Footer is not displayed on the homepage"