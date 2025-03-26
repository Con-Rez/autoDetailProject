from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to chromedriver.exe
chromedriver_path = r"C:\Users\uzma\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe.exe" 
chrome_browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome browser executable

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_browser_path  

# Initialize the WebDriver using the Service class
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Contact Us page
url = "http://127.0.0.1:8000/contact_us/" 
driver.get(url)

# Wait for the page to load
print("Please solve the CAPTCHA manually.")
time.sleep(15)  # Allow time for CAPTCHA to be solved manually

# After CAPTCHA is solved, wait for the form to load
print("Waiting for the form to load...")

try:
  
    iframe_elements = driver.find_elements(By.TAG_NAME, 'iframe')
    if len(iframe_elements) > 0:
        driver.switch_to.frame(iframe_elements[0])  
        print("Switched to iframe.")
    else:
        print("No iframe detected, proceeding directly with the form.")

    # Wait for the form fields to load
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "whsOnd"))) 
    print("Form fields are available.")

    # Find the name input field 
    name_field = driver.find_element(By.XPATH, "//input[@type='text' and @class='whsOnd zHQkBf']")
    name_field.clear()  
    name_field.send_keys("akauto")  

    # Find the email input field 
    email_field = driver.find_element(By.XPATH, "//input[@type='email' and @class='whsOnd zHQkBf']")
    email_field.clear()  
    email_field.send_keys("akautodetail@gmail.com")  

    # Find the message textarea field
    message_field = driver.find_element(By.XPATH, "//textarea[@aria-label='Your answer' and @jsname='YPqjbf']")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Your answer' and @jsname='YPqjbf']")))  
    message_field.clear()  
    message_field.send_keys("this is a message")  

    print("Form filled with name, email, and message.")

    # submit the form 
    submit_button = driver.find_element(By.XPATH, "//span[@class='NPEfkd RveJvd snByac' and text()='Submit']")
    submit_button.click()


    # Wait for a while to inspect the filled form
    time.sleep(5)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    print("Form submitted successfully!")
    time.sleep(5)  
    driver.quit()


    

