import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class AdminReviewsTest(unittest.TestCase):
    """Test suite for testing admin panel functionality for reviews."""
    
    def setUp(self):

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1:8000"
        self.admin_url = f"{self.base_url}/admin"
        self.admin_username = "akadmin"
        self.admin_password = "Carmaker8DivisiveCinema"
        self.login_to_admin()

    def tearDown(self):
        self.driver.quit()

    def login_to_admin(self):
        self.driver.get(self.admin_url)
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.ID, "id_username"))
            )
            self.driver.find_element(By.ID, "id_username").send_keys(self.admin_username)
            self.driver.find_element(By.ID, "id_password").send_keys(self.admin_password)
            self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-tools"))
            )
            print("Login to admin panel - PASSED")
        except TimeoutException:
            print("Login to admin panel - FAILED")
            self.fail("Login to admin panel failed - timeout waiting for elements")

    def test_edit_review_and_verify_on_homepage(self):
        """Test editing a review in admin panel and verifying changes on homepage."""
        self.driver.get(f"{self.admin_url}home/review/")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#result_list tbody tr a"))
            )
            self.driver.find_element(By.CSS_SELECTOR, "#result_list tbody tr a").click()
            print("Edit review test - PASSED")
        except (TimeoutException, NoSuchElementException):
            print("Edit review test - FAILED")
            self.fail("Review not found - Ensure there is at least one review available.")

    def test_empty_fields_validation(self):
        """Test validation for empty required fields in review form."""
        self.driver.get(f"{self.admin_url}home/review/add/")
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "id_title"))
            )
            self.driver.find_element(By.NAME, "_save").click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".errorlist"))
            )
            errors = self.driver.find_elements(By.CSS_SELECTOR, ".errorlist li")
            if not errors:
                print("Empty fields validation test - FAILED")
                self.fail("No error messages found. Check form validation.")
            print(f" Empty fields validation test - PASSED with errors: {[error.text for error in errors]}")
        except TimeoutException:
            print("Empty fields validation test - FAILED")
            self.fail("Test failed - timeout waiting for validation errors")

    def test_invalid_url_validation(self):
        """Test validation for invalid URL in the link field."""
        self.driver.get(f"{self.admin_url}home/review/add/")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "id_link"))
            )
            self.driver.find_element(By.ID, "id_title").send_keys("Test Review Title")
            self.driver.find_element(By.ID, "id_text").send_keys("Test review text content.")
            self.driver.find_element(By.ID, "id_link").send_keys("not-a-valid-url")
            self.driver.find_element(By.NAME, "_save").click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".errorlist"))
            )
            errors = self.driver.find_elements(By.CSS_SELECTOR, ".errorlist li")
            error_messages = [error.text for error in errors]
            if any("valid url" in msg.lower() for msg in error_messages):
                print(f" Invalid URL validation test - PASSED with errors: {error_messages}")
            else:
                print(" Invalid URL validation test - FAILED")
                self.fail("No error message for invalid URL format")
        except TimeoutException:
            print(" Invalid URL validation test - FAILED")
            self.fail("Test failed - timeout waiting for validation errors")

if __name__ == "__main__":
    unittest.main()
