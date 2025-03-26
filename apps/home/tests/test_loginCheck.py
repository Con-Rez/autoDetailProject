from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Setup
URL = "http://127.0.0.1:8000/admin/login/?next=/admin/"  
ValidUsername = "akadmin"
ValidPassword = "Carmaker8DivisiveCinema"
InvalidUsername = "wronguser"
InvalidPassword = "WrongPassword@1234"

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()  

def Valid_Login(username, password):
    driver.get(URL)
    time.sleep(2)
    
    # Locate elements
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    
    # Enter credentials
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    
    time.sleep(3)
    
    # Verify successful login 
    if "dashboard" in driver.current_url or "admin" in driver.current_url:
        print("PASSED: Login with correct credentials successful.")
        return True
    else:
        print("FAILED: Expected login success, but it failed.")
        return False

def Invalid_Login(username, password):
    driver.get(URL)
    time.sleep(2)
    
    # Locate elements
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    
    # Enter invalid credentials
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    
    time.sleep(3)
    
    # Verify failure 
    if driver.current_url == URL or "error" in driver.page_source.lower():
        print("PASSED: Login with incorrect credentials failed as expected.")
        return True
    else:
        print("FAILED: Expected login failure, but it succeeded.")
        return False

# Script Execution
try:
    # Test Valid_Login
    valid_test_passed = Valid_Login(ValidUsername, ValidPassword)
    driver.get("http://127.0.0.1:8000/admin/logout/")  
    time.sleep(2)

    # Test Invalid_Login
    invalid_test_passed = Invalid_Login(InvalidUsername, InvalidPassword)

    # Final test result
    if valid_test_passed and invalid_test_passed:
        print("PASSED: All tests passed.")

except Exception as e:
    print(f"FAILED: Test failed: {e}")

finally:
    driver.quit()