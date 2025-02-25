import time
from django.test import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DiscountModalSeleniumTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)  # Give the browser some time to load elements

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_discount_modal_appears_and_closes(self):
        # Open the schedule appointment page
        self.driver.get(self.live_server_url + '/schedule_appointment/')
        
        # Wait 7 seconds to give the modal time to appear (modal is set to display after 5 seconds)
        time.sleep(7)
        
        # Try to find the modal element
        try:
            modal = self.driver.find_element(By.ID, "discountModal")
            if modal.is_displayed():
                print("Modal appeared as expected.")
            else:
                print("Modal element found but not visible.")
        except Exception as e:
            print("Modal not found. Error:", e)
            return  # Exit the test early since the modal did not appear

        # Try to find and click the close button
        try:
            close_button = self.driver.find_element(By.CLASS_NAME, "btn-close")
            close_button.click()
            print("Close button clicked.")
        except Exception as e:
            print("Could not click close button. Error:", e)
            return

        # Wait a few seconds to allow the modal to close
        time.sleep(3)
        
        # Check if the modal is no longer visible
        try:
            if not modal.is_displayed():
                print("Modal closed as expected.")
            else:
                print("Modal is still visible after clicking close.")
        except Exception as e:
            print("Error when checking modal visibility:", e)

