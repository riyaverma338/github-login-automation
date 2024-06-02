from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Setup the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open GitHub login page
        driver.get('https://github.com/login')

        # Wait for the username field to be present and then enter the username
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
        username.send_keys('vermariya1202@gmail.com')  # Replace with your GitHub username

        # Enter the password
        password = driver.find_element(By.ID, 'password')
        password.send_keys('technology1202')  # Replace with your GitHub password

        # Click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'commit')))
        login_button.click()

        # Wait for the page to load after login
        time.sleep(3)  # Adjust the sleep time as necessary

        # Verify successful login
        profile_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//summary[@aria-label='View profile and more']")))
        print("Login successful!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()
