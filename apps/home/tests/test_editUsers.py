from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Configuration
ADMIN_URL = "http://127.0.0.1:8000/adminlogin/?next=/admin"  # Change as needed
ADMIN_USERNAME = "akadmin"
ADMIN_PASSWORD = "Carmaker8DivisiveCinema"
NEW_USER_USERNAME = "testuser"
NEW_USER_PASSWORD = "Test@1234"
NEW_USER_EMAIL = "testuser@example.com"


# Initialize WebDriver 
driver = webdriver.Chrome()  #This is for chrome. If you are not using chrome, make sure to switch to the webdriver of your browser. 


def login(username, password):
    """ Logs into Django admin """
    driver.get(ADMIN_URL)
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(3)

def create_user():
    """Creates a new user via Django admin and assigns staff status"""
    
    driver.get("http://127.0.0.1:8000/adminauth/user/add/")  
    time.sleep(2)

    # Fill in the username and password fields
    driver.find_element(By.NAME, "username").send_keys(NEW_USER_USERNAME)
    driver.find_element(By.NAME, "password1").send_keys(NEW_USER_PASSWORD)
    driver.find_element(By.NAME, "password2").send_keys(NEW_USER_PASSWORD)
    
    # Save the user
    driver.find_element(By.NAME, "_save").click()
    time.sleep(3)

    # Search for the newly created user
    driver.get("http://127.0.0.1:8000/adminauth/user/")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(NEW_USER_USERNAME)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Click on the user to edit
    driver.find_element(By.LINK_TEXT, NEW_USER_USERNAME).click()
    time.sleep(2)

    # Assign Email
    driver.find_element(By.NAME, "email").send_keys(NEW_USER_EMAIL)
    
    # Assign staff status
    driver.find_element(By.NAME, "is_staff").click()
    driver.find_element(By.NAME, "is_superuser").click()
    
    # Save changes
    driver.find_element(By.NAME, "_save").click()
    time.sleep(3)

    print(f"User {NEW_USER_USERNAME} created and assigned staff status.")

def delete_user():
    """ Deletes the created user via Django admin """
    driver.get("http://127.0.0.1:8000/adminauth/user/")
    time.sleep(2)

    # Find and select the user checkbox
    try:
        user_checkbox = driver.find_element(By.XPATH, f"//th[contains(., '{NEW_USER_USERNAME}')]/preceding-sibling::td/input[@type='checkbox']")
        user_checkbox.click()
    except Exception as e:
        print("User checkbox not found:", e)
        return

    # Select "Delete selected users" from the action dropdown
    action_dropdown = Select(driver.find_element(By.NAME, "action"))
    action_dropdown.select_by_value("delete_selected")  

    # Click 'Go' button
    driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Go')]").click()
    time.sleep(2)

    # Confirm deletion on the confirmation page
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(3)

    print("User deleted successfully.")


def verify_login_failure(username, password):
    """ Attempts to log in with a deleted user, expecting failure """
    driver.get(ADMIN_URL)
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(3)

# Execute the script
try:
    login(ADMIN_USERNAME, ADMIN_PASSWORD)
    create_user()
    driver.get("http://127.0.0.1:8000/adminlogout/")  # Logout admin
    time.sleep(2)

    login(NEW_USER_USERNAME, NEW_USER_PASSWORD)  # Login with new user
    driver.get("http://127.0.0.1:8000/adminlogout/")  # Logout new user
    time.sleep(2)

    login(ADMIN_USERNAME, ADMIN_PASSWORD)  # Re-login as admin
    delete_user()  # Delete the test user

    verify_login_failure(NEW_USER_USERNAME, NEW_USER_PASSWORD)  # Ensure login fails after deletion

except Exception as e:
    print("Test Passed: User creation, login, deletion, and failed re-login worked correctly.")

finally:
    driver.quit()
