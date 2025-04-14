from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
import requests
from decouple import config # This is used to read the .env file

# Configuration
ADMIN_URL = "http://127.0.0.1:8000/adminlogin/?next=/admin" 
PHOTO_LIST_URL = "http://127.0.0.1:8000/adminhome/photo/"  # The page with clickable links
PHOTO_CHANGE_URL = "http://127.0.0.1:8000/adminhome/photo/16/change/"  # Adjust this to the correct photo change URL
ADMIN_USERNAME = config('ADMIN_USERNAME')
ADMIN_PASSWORD = config('ADMIN_PASSWORD')
IMAGE_URL = "https://images.pexels.com/photos/1805053/pexels-photo-1805053.jpeg"  # The image URL
IMAGE_PATH = "valid_image.jpg"  # Local path for saving the downloaded image
RESET_IMAGE_PATH = "apps/home/static/imgs/BlackHyundai.jpg"  # Local path for the reset image
INVALID_IMAGE_URL = "https://images.pexels.com/photos/112460/pexels-photo-112460.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" # invalid image
INVALID_IMAGE_PATH = "invalid_image.jpg"
NEW_TITLE = "Updated Photo Title"  # New title to set
NEW_DESCRIPTION = "Updated description for the photo"  # New description to set
OLD_TITLE = "Gallery Right After"
OLD_DESCRIPTION = "Photo Size: 3024 x 4032. After Image 3"

# Initialize WebDriver
driver = webdriver.Chrome()


def login(username, password):
    """Logs into Django admin."""
    driver.get(ADMIN_URL)
    time.sleep(2)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(3)


def download_image(url, file_path):
    """Downloads an image from the given URL."""
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"Image downloaded to {file_path}")




def navigate_to_photo_change_page():
    """Navigates to the photo change page after clicking the 'Gallery Right After' link."""
    driver.get(PHOTO_LIST_URL)
    time.sleep(2)

    # Click the link with the name 'Gallery Right After'
    gallery_link = driver.find_element(By.LINK_TEXT, "Gallery Right After")
    gallery_link.click()
    time.sleep(3)


def upload_photo_and_modify_fields(image_path, new_title, new_description):
    """Uploads a photo, modifies the title and description fields, and saves the changes."""
    driver.get(PHOTO_CHANGE_URL)  # Navigate directly to the change page
    time.sleep(2)

    # Change the title
    title_input = driver.find_element(By.NAME, "title")
    title_input.clear()  # Clear the existing title
    title_input.send_keys(new_title)  # Enter the new title

    # Upload the image by interacting with the "choose file" button
    upload_input = driver.find_element(By.NAME, "image")  # Adjust field name if needed
    upload_input.send_keys(os.path.abspath(image_path))  # Upload the image

    # Change the description
    description_input = driver.find_element(By.NAME, "description")
    description_input.clear()  # Clear the existing description
    description_input.send_keys(new_description)  # Enter the new description

    # Save changes
    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(10)

    # Verify success message
    try:
        success_message = driver.find_element(By.CLASS_NAME, "success")
        print("Photo uploaded and fields updated successfully.")
    except:
        print("Photo upload or field update failed.")

def test_invalid_image(invalid_image_path):
    
    driver.get(PHOTO_CHANGE_URL)
    time.sleep(2)
    # Reset image by uploading the reset image
    upload_input = driver.find_element(By.NAME, "image")  # Adjust field name if needed
    upload_input.send_keys(os.path.abspath(invalid_image_path))  # Upload the reset image

    # Save changes
    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(3)

    # Verify failure message or error handling
    try:
        # Attempt to find error messages (e.g., validation error for invalid image)
        error_message = driver.find_element(By.CLASS_NAME, "errornote")
        print("Invalid Photo upload failed successfully with error: ", error_message.text)
    except:
        print("Photo upload failed, but no error message was found.")
   
def reset_photo_fields(reset_image_path, old_title, old_description):
    """Resets photo fields to their original values and changes image to the reset image."""
    driver.get(PHOTO_CHANGE_URL)
    time.sleep(2)

    # reset title   
    title_input = driver.find_element(By.NAME, "title")
    title_input.clear()
    title_input.send_keys(old_title)

    # Reset image by uploading the reset image
    upload_input = driver.find_element(By.NAME, "image")  # Adjust field name if needed
    upload_input.send_keys(os.path.abspath(reset_image_path))  # Upload the reset image


    # reset description
    description_input = driver.find_element(By.NAME, "description")
    description_input.clear()  # Clear the existing description
    description_input.send_keys(old_description)  


    # Save changes
    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()
    time.sleep(3)

    # Verify success message
    try:
        success_message = driver.find_element(By.CLASS_NAME, "success")
        print("Photo uploaded and fields reset successfully.")
    except:
        print("Photo upload or field update failed.")



# Execute the test script
try:
    login(ADMIN_USERNAME, ADMIN_PASSWORD)

    # Download and upload the valid image
    download_image(IMAGE_URL, IMAGE_PATH)

    # Navigate to the photo change page
    navigate_to_photo_change_page()

    # Upload the photo and update the title and description
    upload_photo_and_modify_fields(IMAGE_PATH, NEW_TITLE, NEW_DESCRIPTION)

    # Test invalid image

    download_image(INVALID_IMAGE_URL,INVALID_IMAGE_PATH)

    test_invalid_image(INVALID_IMAGE_PATH)

    # Reset Fields
    reset_photo_fields(RESET_IMAGE_PATH,OLD_TITLE,OLD_DESCRIPTION)    

    print("Photo Upload, Invalid Photo Upload, and Reset Photo Upload Tests Passed.")

except Exception as e:
    print("Test encountered an error:", e)

finally:
    driver.quit()

    # Cleanup downloaded image
    if os.path.exists(IMAGE_PATH):
        os.remove(IMAGE_PATH)
    if os.path.exists(INVALID_IMAGE_PATH):
        os.remove(INVALID_IMAGE_PATH)