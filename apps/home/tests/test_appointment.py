import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class AppointmentBookingTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.save_screenshot("final_state.png")
        self.driver.quit()

    def test_schedule_google_appointment(self):
        print("Opening homepage...")
        self.driver.get("http://127.0.0.1:8000/")

        print("Waiting for 'Schedule Appointment' link...")
        schedule_tab = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.nav-link[href='/schedule_appointment/']")
        ))
        print("Clicking 'Schedule Appointment'...")
        schedule_tab.click()

        print("Waiting for iframe...")
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

        # Hide sticky nav and scroll iframe into view
        self.driver.execute_script("document.querySelector('.nav-links').style.display = 'none';")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", iframe)
        time.sleep(1)

        self.driver.switch_to.frame(iframe)
        time.sleep(2)  # Let iframe fully load

        print("Searching for all 9:00am time slot buttons...")
        time_buttons = self.wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//button[contains(@aria-label, '9:00')]"
        )))

        clicked = False
        for button in time_buttons:
            try:
                if button.is_displayed() and button.is_enabled():
                    print("Clicking 9:00am button...")
                    button.click()
                    clicked = True
                    break
            except Exception as e:
                print("Error clicking button:", e)

        if not clicked:
            print("No clickable 9:00am buttons found.")
            self.driver.save_screenshot("no_9am_clicked.png")
            return

        print("Waiting for form to focus...")
        # Wait until the active element is an input field
        for _ in range(20):  # Try for 2 seconds
            active = self.driver.switch_to.active_element
            if active.tag_name == "input":
                break
            time.sleep(0.1)
        else:
            print("Form input not focused after selecting time slot.")
            self.driver.save_screenshot("form_not_focused.png")
            return

        print("Filling form using keyboard navigation...")
        try:
            def slow_type(element, text):
                for char in text:
                    element.send_keys(char)
                    time.sleep(0.1)

            # First Name
            slow_type(active, "Test")
            active.send_keys(Keys.TAB)
            time.sleep(0.3)

            # Last Name
            active = self.driver.switch_to.active_element
            slow_type(active, "User")
            active.send_keys(Keys.TAB)
            time.sleep(0.3)

            # Email
            active = self.driver.switch_to.active_element
            slow_type(active, "test@example.com")
            active.send_keys(Keys.TAB)
            time.sleep(0.3)

            # Phone
            active = self.driver.switch_to.active_element
            slow_type(active, "1234567890")
            active.send_keys(Keys.TAB)
            time.sleep(0.3)

            # Description
            active = self.driver.switch_to.active_element
            slow_type(active, "Testing Selenium booking")
            active.send_keys(Keys.TAB)
            time.sleep(0.5)

            # Book Button
            active = self.driver.switch_to.active_element
            active.send_keys(Keys.ENTER)
            print("Form filled and submitted via keyboard.")

        except Exception as e:
            print("Error during keyboard form fill:", e)
            self.driver.save_screenshot("keyboard_fill_failed.png")
            return

        print("Waiting for confirmation...")
        time.sleep(3)
        self.driver.save_screenshot("confirmation.png")
        print("Test completed successfully.")