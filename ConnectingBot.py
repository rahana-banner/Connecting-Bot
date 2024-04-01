from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

# Set the path to GeckoDriver executable
geckodriver_path = "C:\\Users\\karbo\\geckodriver.exe"

# Create FirefoxOptions object
options = Options()
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Specify the path to Firefox binary if not in PATH

# Set the path to GeckoDriver executable in options
options.binary_location = geckodriver_path

# Initialize the WebDriver with FirefoxOptions
driver = webdriver.Firefox(options=options)

# Open LinkedIn login page
driver.get("https://www.linkedin.com")

# Log in
time.sleep(2)

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

# ***ACCOUNT CREDENTIALS***
# username.send_keys('bbanushree6@gmail.com')
# time.sleep(2)
# password.send_keys('Banu@Shree@8')

username.send_keys('dakac50192@nimadir.com')
time.sleep(2)
password.send_keys('demo@12345')
time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

# # Wait until the submit button with type="submit" is clickable
# WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
# )

# dakac50192@nimadir.com - demo@12345

# Add contacts
time.sleep(30)
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=Evz")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(4)
    send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
    # driver.execute_script("arguments[0].click();", send)
    # close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
    # driver.execute_script("arguments[0].click();", close)
    # time.sleep(2)
    
    # Click "Add a note"
    add_note_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add a note']"))
    )
    add_note_button.click()

    # Enter the note
    note_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "message")))
    note = "Hi, let's connect!"
    note_field.send_keys(note)
    time.sleep(2)

    # Send the invitation
    send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
    send_button.click()

    # Optionally, wait a moment before sending the next invite to mimic human behavior and avoid rate limits
    WebDriverWait(driver, 2).until(lambda d: True) 