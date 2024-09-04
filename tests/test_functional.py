import sys
import os
import pytest
from utils.base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestFunctional(BaseTest):
    @pytest.mark.usefixtures("setup")
    def test_search_add_to_cart_checkout(self):
        self.driver.get("https://www.saucedemo.com/")
        
        # Login
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce", Keys.RETURN)
        
        # Verify successful login
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory.html")
        )
        
        # Adding item to cart
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        ).click()
        
        # Go to cart
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Verify the product is added to the cart
        product_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert product_name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack' but got '{product_name}'"
        
        # Proceed to checkout
        self.driver.find_element(By.ID, "checkout").click()
        
        self.driver.find_element(By.ID, "first-name").send_keys("Arjun")
        self.driver.find_element(By.ID, "last-name").send_keys("Nagendhra")
        self.driver.find_element(By.ID, "postal-code").send_keys("572101")
        self.driver.find_element(By.ID, "continue").click()

        # Verify checkout step 2 is reached
        assert "checkout-step-two.html" in self.driver.current_url
