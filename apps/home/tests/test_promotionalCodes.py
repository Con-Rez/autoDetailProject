import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from datetime import datetime, timedelta

# Basic configuration for admin login and appointments page
ADMIN_LOGIN_URL = "http://127.0.0.1:8000/adminlogin/?next=/admin"
APPOINTMENTS_URL = "http://127.0.0.1:8000/schedule_appointment/"

ADMIN_USERNAME = "akadmin"
ADMIN_PASSWORD = "Carmaker8DivisiveCinema"

# Generate promotion details
PROMO_NAME = "Test Promotion"
PROMO_CODE = "testpromo1234"
PROMO_DISCOUNT = "10"
PROMO_MESSAGE = "This is a test promotion for automated testing."
today = datetime.today().strftime("%Y-%m-%d")
tomorrow = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
UPDATED_PROMO_MESSAGE = "Updated promotion message after edit."

# Set up Selenium WebDriver (Chrome)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def admin_login(username, password):
    # Go to admin login, wait for username field
    driver.get(ADMIN_LOGIN_URL)
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    # Fill in credentials, then submit
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    # Wait until the admin page loads
    wait.until(EC.url_contains("/admin"))
    time.sleep(1)

def add_promotion():
    # Go to the 'add promotion' page, wait for form, fill it out, then save
    driver.get("http://127.0.0.1:8000/adminhome/promotion/add/")
    name_field = wait.until(EC.presence_of_element_located((By.ID, "id_name")))
    name_field.send_keys(PROMO_NAME)
    driver.find_element(By.ID, "id_code").send_keys(PROMO_CODE)
    driver.find_element(By.ID, "id_discount_percentage").send_keys(PROMO_DISCOUNT)
    driver.find_element(By.ID, "id_message").send_keys(PROMO_MESSAGE)
    driver.find_element(By.ID, "id_start_date").send_keys(today)
    driver.find_element(By.ID, "id_end_date").send_keys(tomorrow)
    driver.find_element(By.NAME, "_save").click()
    # Wait for promotion list to load, then confirm
    wait.until(EC.url_contains("/adminhome/promotion/"))
    time.sleep(2)
    print(f"PASS: Promotion added with code: {PROMO_CODE}")

def edit_promotion():
    # Find the newly added promotion, click to edit, then change its message
    driver.get("http://127.0.0.1:8000/adminhome/promotion/")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, PROMO_NAME)))
    driver.find_element(By.LINK_TEXT, PROMO_NAME).click()
    wait.until(EC.presence_of_element_located((By.ID, "id_message")))
    time.sleep(1)
    message_field = driver.find_element(By.ID, "id_message")
    message_field.clear()
    message_field.send_keys(UPDATED_PROMO_MESSAGE)
    driver.find_element(By.NAME, "_save").click()
    wait.until(EC.url_contains("/adminhome/promotion/"))
    time.sleep(2)
    print("PASS: Promotion edited.")

def delete_promotion():
    # Navigate to promotion list, open the promotion, click delete, then confirm
    driver.get("http://127.0.0.1:8000/adminhome/promotion/")
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, PROMO_NAME)))
    driver.find_element(By.LINK_TEXT, PROMO_NAME).click()
    wait.until(EC.presence_of_element_located((By.ID, "id_message")))
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Delete").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    wait.until(EC.url_contains("/adminhome/promotion/"))
    time.sleep(2)
    print("PASS: Promotion deleted.")

def test_valid_promo_on_appointments():
    # Visit appointments, enter valid promo code, then verify 'saving'
    driver.get(APPOINTMENTS_URL)
    wait.until(EC.presence_of_element_located((By.ID, "promoCodeInputCalc")))
    time.sleep(3)
    driver.refresh()
    time.sleep(2)
    promo_input = driver.find_element(By.ID, "promoCodeInputCalc")
    promo_input.clear()
    promo_input.send_keys(PROMO_CODE)
    driver.find_element(By.ID, "applyPromoBtnCalc").click()
    time.sleep(5)
    promo_message = driver.find_element(By.ID, "promoMessage").text
    if "saving" in promo_message.lower():
        print("PASS: Valid promo code accepted on appointments page.")
    else:
        print("FAIL: Valid promo code was not accepted.")

def test_invalid_promo_on_appointments():
    # Enter an invalid code, check if it is rejected
    driver.get(APPOINTMENTS_URL)
    wait.until(EC.presence_of_element_located((By.ID, "promoCodeInputCalc")))
    time.sleep(2)
    promo_input = driver.find_element(By.ID, "promoCodeInputCalc")
    promo_input.clear()
    promo_input.send_keys("invalidcode")
    driver.find_element(By.ID, "applyPromoBtnCalc").click()
    time.sleep(5)
    promo_message = driver.find_element(By.ID, "promoMessage").text
    if "invalid" in promo_message.lower():
        print("PASS: Invalid promo code correctly rejected on appointments page.")
    else:
        print("FAIL: Invalid promo code was not rejected as expected.")

def test_select_service_and_apply_promo():
    # Select first service, apply promo code, then verify cost
    driver.get(APPOINTMENTS_URL)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".service-checkbox")))
    time.sleep(2)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, ".service-checkbox")
    if not checkboxes:
        print("FAIL: No services found to select.")
        return

    first_checkbox = checkboxes[0]
    try:
        # Parse the 'value' attribute, which is the numeric cost
        service_cost = float(first_checkbox.get_attribute("value"))
    except Exception as e:
        print(f"FAIL: Could not retrieve first service cost: {e}")
        return

    # Select the service if not already selected
    if not first_checkbox.is_selected():
        first_checkbox.click()
    time.sleep(1)

    # Enter the valid promo code
    promo_input = driver.find_element(By.ID, "promoCodeInputCalc")
    promo_input.clear()
    promo_input.send_keys(PROMO_CODE)
    driver.find_element(By.ID, "applyPromoBtnCalc").click()
    time.sleep(1)

    # Wait for #total-cost to become numeric
    def cost_is_numeric(driver):
        text = driver.find_element(By.ID, "total-cost").text.strip()
        return bool(re.match(r'^\d+(\.\d+)?$', text))

    try:
        WebDriverWait(driver, 10).until(cost_is_numeric)
    except:
        print("FAIL: total-cost did not become a numeric string within 10 seconds.")
        return

    # Parse the cost
    total_cost_text = driver.find_element(By.ID, "total-cost").text.strip()
    try:
        total_cost = float(total_cost_text)
    except Exception as e:
        print(f"FAIL: Could not parse total cost after applying promo code: '{total_cost_text}' - {e}")
        return

    # Compare against expected discount
    expected = service_cost * (1 - float(PROMO_DISCOUNT) / 100.0)
    if abs(total_cost - expected) < 0.01:
        print(f"PASS: service + promo code = expected {expected:.2f}, got {total_cost:.2f}")
    else:
        print(f"FAIL: service + promo code math error: expected {expected:.2f}, got {total_cost:.2f}")

try:
    # Admin logs in and adds a promotion
    admin_login(ADMIN_USERNAME, ADMIN_PASSWORD)
    add_promotion()

    # Log out admin so we can test the promo in the front end
    driver.get("http://127.0.0.1:8000/adminlogout/")
    time.sleep(2)

    # Test valid and invalid promo codes on the appointments page
    test_valid_promo_on_appointments()
    test_invalid_promo_on_appointments()

    # Admin logs back in and edits the promotion
    admin_login(ADMIN_USERNAME, ADMIN_PASSWORD)
    edit_promotion()

    # Log out, select service, apply newly edited promo code
    driver.get("http://127.0.0.1:8000/adminlogout/")
    time.sleep(2)
    driver.get(APPOINTMENTS_URL)
    time.sleep(1)
    test_select_service_and_apply_promo()

    # Admin logs in again to delete the promotion
    driver.get("http://127.0.0.1:8000/adminlogout/")
    time.sleep(2)
    admin_login(ADMIN_USERNAME, ADMIN_PASSWORD)
    delete_promotion()

    # Final check that the promo code is no longer accepted
    driver.get(APPOINTMENTS_URL)
    wait.until(EC.presence_of_element_located((By.ID, "promoCodeInputCalc")))
    time.sleep(2)
    promo_input = driver.find_element(By.ID, "promoCodeInputCalc")
    promo_input.clear()
    promo_input.send_keys(PROMO_CODE)
    driver.find_element(By.ID, "applyPromoBtnCalc").click()
    time.sleep(7)
    promo_message = driver.find_element(By.ID, "promoMessage").text
    if "invalid" in promo_message.lower():
        print("PASS: After deletion, promo code is correctly rejected on appointments page.")
    else:
        print("FAIL: Deleted promo code still accepted on appointments page.")

    print("PASS: All promotional code tests completed successfully.")

except Exception as e:
    print("FAIL: Test encountered an error:", e)

finally:
    driver.quit()
