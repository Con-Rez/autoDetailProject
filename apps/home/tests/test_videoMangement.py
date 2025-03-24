import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
from selenium.webdriver.chrome.options import Options

class VideoUploadTests(unittest.TestCase):

    def setUp(self):
        """Setup the WebDriver and configuration."""
        self.ADMIN_URL = "http://127.0.0.1:8000/adminlogin/?next=/admin"
        self.VIDEO_ADD_URL = "http://127.0.0.1:8000/adminhome/transformationvideo/add/"
        self.VIDEO_LIST_URL = "http://127.0.0.1:8000/adminhome/transformationvideo/"
        self.GALLERY_URL = "http://127.0.0.1:8000/gallery/"

        self.ADMIN_USERNAME = "akadmin"
        self.ADMIN_PASSWORD = "Carmaker8DivisiveCinema"

        self.VALID_VIDEO_URL = "https://www.w3schools.com/html/mov_bbb.mp4"
        self.VALID_VIDEO_PATH = "valid_video.mp4"
        self.INVALID_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Iconic_image_of_earth.jpg/800px-Iconic_image_of_earth.jpg"
        self.INVALID_IMAGE_PATH = "invalid_image.jpg"
        self.NEW_TITLE = "Test Transformation Image"
        self.NEW_DESCRIPTION = "This is a test transformation image."

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-cache")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.test_result = True  # Track the overall result

    def login(self, username, password):
        """Logs into Django admin."""
        self.driver.get(self.ADMIN_URL)
        time.sleep(2)

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        time.sleep(3)

    def download_file(self, url, file_path):
        """Downloads a file from the given URL if it doesn't already exist."""
        if os.path.exists(file_path):
            print(f"File already exists: {file_path}. Skipping download.")
        else:
            response = requests.get(url, stream=True)
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"File downloaded to {file_path}")

    def add_new_video(self, file_path, title, description):
        """Adds a new video entry."""
        self.driver.get(self.VIDEO_ADD_URL)
        time.sleep(2)

        title_input = self.driver.find_element(By.NAME, "title")
        title_input.send_keys(title)

        upload_input = self.driver.find_element(By.NAME, "video")
        upload_input.send_keys(os.path.abspath(file_path))

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys(description)

        save_button = self.driver.find_element(By.NAME, "_save")
        save_button.click()
        time.sleep(5)

    def verify_video_in_gallery(self, video_file):
        """Verifies the specified video appears in the gallery."""
        self.driver.get(self.GALLERY_URL)
        time.sleep(3)
        self.driver.execute_script("location.reload(true);")  # Hard refresh to prevent caching issues
        time.sleep(3)

        try:
            self.driver.find_element(By.XPATH, f"//video/source[contains(@src, '{video_file}')]")
            print(f"Passed: Video {video_file} successfully appears in the gallery.")
        except:
            self.test_result = False  # Mark test as failed
            print(f"Failed: Video {video_file} not found in the gallery.")

    def try_to_replace_video_with_image(self, image_path):
        """Tries to replace a video with an image and confirms the error."""
        self.driver.get(self.VIDEO_ADD_URL)
        time.sleep(2)

        title_input = self.driver.find_element(By.NAME, "title")
        title_input.send_keys(self.NEW_TITLE)

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.send_keys(self.NEW_DESCRIPTION)

        upload_input = self.driver.find_element(By.NAME, "video")
        upload_input.send_keys(os.path.abspath(image_path))

        save_button = self.driver.find_element(By.NAME, "_save")
        save_button.click()
        time.sleep(5)

        try:
            self.driver.find_element(By.CLASS_NAME, "error")
            print("Failed: Image was able to be saved.")
        except:
            self.test_result = True  # Mark test as Passed
            print("Passed: Error saving with invalid format as expected.")

    def delete_video(self):
        """Deletes the video from the admin panel."""
        self.driver.get(self.VIDEO_LIST_URL)
        time.sleep(2)

        try:
            checkbox = self.driver.find_element(By.NAME, "_selected_action")
            checkbox.click()

            action_dropdown = self.driver.find_element(By.NAME, "action")
            action_dropdown.send_keys("delete_selected")

            go_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Go')]")
            go_button.click()
            time.sleep(2)

            confirm_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
            confirm_button.click()
            time.sleep(3)

            print("Passed: Video deleted successfully.")
        except Exception as e:
            self.test_result = False  # Mark test as failed
            print(f"Failed: Failed to delete video: {e}.")

    def test_video_upload(self):
        self.login(self.ADMIN_USERNAME, self.ADMIN_PASSWORD)

        # Add new video
        self.download_file(self.VALID_VIDEO_URL, self.VALID_VIDEO_PATH)
        self.add_new_video(self.VALID_VIDEO_PATH, self.NEW_TITLE, self.NEW_DESCRIPTION)
        self.verify_video_in_gallery("valid_video.mp4")

        # Try to replace video with an image and check for error
        self.download_file(self.INVALID_IMAGE_URL, self.INVALID_IMAGE_PATH)
        self.try_to_replace_video_with_image(self.INVALID_IMAGE_PATH)

        # Delete the video
        self.delete_video()

        # Output the final result
        if self.test_result:
            print("Overall Test Result: PASSED")
        else:
            print("Overall Test Result: FAILED")

    def tearDown(self):
        self.driver.quit()

        if os.path.exists(self.VALID_VIDEO_PATH):
            os.remove(self.VALID_VIDEO_PATH)
        if os.path.exists(self.INVALID_IMAGE_PATH):
            os.remove(self.INVALID_IMAGE_PATH)

if __name__ == "__main__":
    unittest.main()