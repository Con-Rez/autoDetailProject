from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the ChromeDriver path
chromedriver_path= r"C:\Users\uzma\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe.exe"

# Configure Chrome WebDriver service and options
service = Service(chromedriver_path)
options = Options()
options.add_argument("--start-maximized")  # Start Chrome in maximized mode


# WebDriver (Chrome)
driver = webdriver.Chrome(service=service, options=options)

try:
   
    base_url = "http://127.0.0.1:8000"  
    pages = ["/", "/about/", "/contact_us/"]  

    for page in pages:
        url = base_url + page
        print(f"Opening: {url}")
        driver.get(url)  
        time.sleep(2)  # Wait for the page to load

        # Resize the window to test responsiveness*
        driver.set_window_size(1200, 800)  
        print(f"Resized window for: {url}")
        time.sleep(1) 

        # Scroll down to bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Scrolled to bottom of: {url}")
        time.sleep(2)  

        # Scroll back up to the top
        driver.execute_script("window.scrollTo(0, 0);")
        print(f"Scrolled back to top of: {url}")
        time.sleep(1)  # Pause

    print("Task complete: Resized and scrolled through the pages.")

except Exception as e:
    print(f" Error: {e}")

finally:
    time.sleep(3)  # Keep the browser open briefly before closing
    driver.quit()  # Close the browser
    print("Browser closed.")
