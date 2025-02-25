# test_dismodal.py

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiscountModalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Uncomment to run headless
        cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_discount_modal_popup(self):
        # Adjust the URL path if necessary.
        url = self.live_server_url + "/schedule_appointment/"
        self.driver.get(url)
        
        # Wait up to 10 seconds for the discount modal to become visible.
        discount_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "discountModal"))
        )
        
        # Assert that the modal is displayed.
        self.assertTrue(discount_modal.is_displayed(), "Discount modal should be visible after the delay.")
