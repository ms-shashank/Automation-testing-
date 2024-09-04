# Automation Testing for ([Swag Labs](https://www.saucedemo.com/))

## Setup
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Execute the tests with Pytest `pytest --alluredir=allure-results`.

## Test Structure
- **Login Test**: Validates login functionality with valid and invalid credentials.
- **Cart & Checkout Test**: Tests the ability to search for a product, add it to the cart, and proceed to checkout.
- **UI Elements Test**: Ensures key UI elements are present and functional on the homepage.
- **Form Validation Test**: Checks the form validation for the contact form.

## Reports
Test reports will be generated in `allure-report/index.html`.
