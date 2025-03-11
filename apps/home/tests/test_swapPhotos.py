from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Configuration
ADMIN_URL = "http://127.0.0.1:8000/adminlogin/?next=/admin"  # Change as needed
ADMIN_USERNAME = "akadmin"
ADMIN_PASSWORD = "Carmaker8DivisiveCinema"



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