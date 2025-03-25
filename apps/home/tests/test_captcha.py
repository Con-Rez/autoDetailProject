from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_captcha_form(driver, url, page_name, success_text, failure_text):
    driver.get(url)
    print(f"\nTesting CAPTCHA on: {page_name}")
    print("Please solve the CAPTCHA manually. You have 10 seconds...")
    time.sleep(10)

    try:
        submit_button = driver.find_element(By.CSS_SELECTOR, "form button[type='submit']")
        submit_button.click()
        print("CAPTCHA Submitted.")
        time.sleep(3)

        # First check for failure message
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), \"{failure_text}\")]"))
            )
            print(f"Test Failed: '{failure_text}' was displayed.")
            return
        except:
            pass  # Failure message not found

        # Then check for success message
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), \"{success_text}\")]"))
            )
            print(f"Test Passed: '{success_text}' was displayed.")
        except:
            print(f"Test Inconclusive: Neither success nor failure message was found.")

    except Exception as e:
        print(f"Test Failed on {page_name}: {str(e)}")

# Start browser
driver = webdriver.Chrome()

# Test for Schedule Appointment page
test_captcha_form(
    driver,
    "http://127.0.0.1:8000/schedule_appointment/",
    "Schedule Appointment",
    success_text="Captcha validation succeeded. Please schedule your appointment.",
    failure_text="Please complete the captcha to schedule an appointment. There's four letters, and they're all capitals"
)

# Test for Contact Us page
test_captcha_form(
    driver,
    "http://127.0.0.1:8000/contact_us/",
    "Contact Us",
    success_text="Captcha validation succeeded. Please proceed to fill out the form.",
    failure_text="Please complete the captcha to proceed. There's four letters, and they're all capitals."
)

# Pause before closing browser
time.sleep(5)
driver.quit()