import pytest
from selenium import webdriver

class BaseTest:
    @pytest.fixture(scope="class")
    def setup(self, request):
        self.driver = webdriver.Chrome()  # Or another browser driver if needed
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
