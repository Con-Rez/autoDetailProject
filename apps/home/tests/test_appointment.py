from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class appointment_test(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
  
    def tearDown(self):
        self.driver.quit()
  
    def test_calendartest(self):
        self.driver.get("http://127.0.0.1:8000/schedule_appointment/")
        self.driver.set_window_size(1141, 692)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        self.driver.find_element(By.ID, "c8").send_keys("Test")
        self.driver.find_element(By.ID, "c9").send_keys("Tester")
        self.driver.find_element(By.ID, "c10").click()
        self.driver.find_element(By.ID, "c10").send_keys("a@example.com")
        self.driver.find_element(By.ID, "c11").click()
        self.driver.find_element(By.ID, "c11").send_keys("1234566789")
        self.driver.find_element(By.ID, "c12").click()
        self.driver.find_element(By.ID, "c12").send_keys("appointment test")
        self.driver.find_element(By.CSS_SELECTOR, ".YUhpIc-vQzf8d").click()

    def no_description_test(self):
        self.driver.get("http://127.0.0.1:8000/schedule_appointment/")
        self.driver.set_window_size(1141, 692)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        self.driver.find_element(By.ID, "c8").send_keys("Test")
        self.driver.find_element(By.ID, "c9").send_keys("Tester")
        self.driver.find_element(By.ID, "c10").click()
        self.driver.find_element(By.ID, "c10").send_keys("a@example.com")
        self.driver.find_element(By.ID, "c11").click()
        self.driver.find_element(By.ID, "c11").send_keys("1234566789")
        self.driver.find_element(By.ID, "c12").click()
        #self.driver.find_element(By.ID, "c12").send_keys("appointment test")
        self.driver.find_element(By.CSS_SELECTOR, ".YUhpIc-vQzf8d").click()
  
