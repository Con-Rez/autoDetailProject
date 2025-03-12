
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL="http://127.0.0.1:8000/schedule_appointment/"


class cost_calc_test(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()



    def test1(self):
        driver = self.driver
        driver.get(URL)

        #driver.implicitly_wait(3)
        #time.sleep(6)
        #close = driver.find_element(by=By.CLASS_NAME, value="btn-close")
        #close.click()
        #time.sleep(2)

        expectedCost = 123.00
        expectedTime = 1.00

        service1 = driver.find_element(by=By.ID, value="service1")
        service1.click()

        cost_element = driver.find_element(by=By.ID, value="total-cost")
        time_element = driver.find_element(by=By.ID, value="total-time")

        cost = float(cost_element.text.strip())
        time_est = float(time_element.text.strip())

        self.assertEqual(cost, expectedCost, f"Expected cost {expectedCost}, but got {cost}")
        self.assertEqual(time_est, expectedTime, f"Expected time {expectedTime}, but got {time_est}")

    def test2(self):
        driver = self.driver
        driver.get(URL)

        dark = driver.find_element(by=By.ID, value="dark-mode-toggle")
        dark.click()

        expectedCost = 579.00
        expectedTime = 3.00

        service1 = driver.find_element(by=By.ID, value="service1")
        service1.click()
        service2 = driver.find_element(by=By.ID, value="service2")
        service2.click()

        cost_element = driver.find_element(by=By.ID, value="total-cost")
        time_element = driver.find_element(by=By.ID, value="total-time")

        cost = float(cost_element.text.strip())
        time_est = float(time_element.text.strip())

        self.assertEqual(cost, expectedCost, f"Expected cost {expectedCost}, but got {cost}")
        self.assertEqual(time_est, expectedTime, f"Expected time {expectedTime}, but got {time_est}")

    def test_promo(self):
        driver = self.driver
        driver.get(URL)

        dark = driver.find_element(by=By.ID, value="dark-mode-toggle")
        dark.click()

        expectedCost = 550.05
        expectedTime = 3.00

        service1 = driver.find_element(by=By.ID, value="service1")
        service1.click()
        service2 = driver.find_element(by=By.ID, value="service2")
        service2.click()

        promo = driver.find_element(by=By.ID, value="promoCodeInputCalc")
        promo.send_keys("PROMO5")
        apply = driver.find_element(by=By.ID, value="applyPromoBtnCalc")
        apply.click()

        cost_element = driver.find_element(by=By.ID, value="total-cost")
        time_element = driver.find_element(by=By.ID, value="total-time")

        cost = float(cost_element.text.strip())
        time_est = float(time_element.text.strip())

        self.assertEqual(cost, expectedCost, f"Expected cost {expectedCost}, but got {cost}")
        self.assertEqual(time_est, expectedTime, f"Expected time {expectedTime}, but got {time_est}")

    def test_promo_fail(self):
        driver = self.driver
        driver.get(URL)

        dark = driver.find_element(by=By.ID, value="dark-mode-toggle")
        dark.click()

        expectedCost = 579.00
        expectedTime = 3.00

        service1 = driver.find_element(by=By.ID, value="service1")
        service1.click()
        service2 = driver.find_element(by=By.ID, value="service2")
        service2.click()

        promo = driver.find_element(by=By.ID, value="promoCodeInputCalc")
        promo.send_keys("PROMO7")
        apply = driver.find_element(by=By.ID, value="applyPromoBtnCalc")
        apply.click()

        cost_element = driver.find_element(by=By.ID, value="total-cost")
        time_element = driver.find_element(by=By.ID, value="total-time")

        cost = float(cost_element.text.strip())
        time_est = float(time_element.text.strip())

        self.assertEqual(cost, expectedCost, f"Expected cost {expectedCost}, but got {cost}")
        self.assertEqual(time_est, expectedTime, f"Expected time {expectedTime}, but got {time_est}")

    def test_reset(self):
        driver = self.driver
        driver.get(URL)

        dark = driver.find_element(by=By.ID, value="dark-mode-toggle")
        dark.click()

        expectedCost = 0.00
        expectedTime = 0.00

        service1 = driver.find_element(by=By.ID, value="service1")
        service1.click()
        service2 = driver.find_element(by=By.ID, value="service2")
        service2.click()

        time.sleep(1)
        service1.click()
        service2.click()


        cost_element = driver.find_element(by=By.ID, value="total-cost")
        time_element = driver.find_element(by=By.ID, value="total-time")

        cost = float(cost_element.text.strip())
        time_est = float(time_element.text.strip())

        self.assertEqual(cost, expectedCost, f"Expected cost {expectedCost}, but got {cost}")
        self.assertEqual(time_est, expectedTime, f"Expected time {expectedTime}, but got {time_est}")



    def tearDown(self):
        # Close the WebDriver after the test
        self.driver.quit()
