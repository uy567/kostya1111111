from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the correct path to your chromedriver
chromedriver_path = r'C:\Users\User\Desktop\Script\chromedriver.exe'  # Update this to the actual path

# Setting up ChromeDriver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get("https://holesky.gasp.xyz/")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)

# Click the 'Get Started' button
get_started_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.box-border")))
get_started_button.click()

# Wait and click on the 'Open' button to initiate Metamask connection
open_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.text-secondary")))
open_button.click()

# This step assumes manual interaction with Metamask
time.sleep(10)  # Adjust this delay based on your interaction speed with Metamask

# Navigate to the 'Deposit' page
deposit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.text-primary")))
deposit_button.click()

# Select the token type
select_token_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.font-semibold")))
select_token_button.click()

# Assuming 'GETH' is the text of the button for selecting GETH token
geth_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'GETH')]")))
geth_button.click()

# Enter the amount to be deposited
input_field = driver.find_element(By.CSS_SELECTOR, "input[data-testid='tokenInput-input']")
input_field.send_keys("10")

# Confirm the deposit
submit_deposit_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-deposit-button']")
submit_deposit_button.click()

# Handle Metamask popup manually to confirm the transaction
time.sleep(10)  # Adjust this to wait for your manual confirmation

# After transaction confirmation, if there is an understanding button
try:
    ok_understand_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Ok, I understand')]")))
    ok_understand_button.click()
except Exception as e:
    print("Ok, I understand button not found or not clickable", e)

# Close the browser
driver.quit()
