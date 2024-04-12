import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome web driver
driver = webdriver.Chrome()

# Pause for 5 seconds to observe browser actions
time.sleep(5)

# Open a specific webpage
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Find the text area element on the webpage
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Enter text into the found text area
textarea.send_keys("get()")
time.sleep(5)

# Find the submit button element
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Click the submit button
submit_button.click()
time.sleep(5)

# Close the browser window
driver.quit()

