from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from os import getenv
from time import sleep
import os
load_dotenv()
EMAIL = getenv('EMAIL')
               
PASSWORD = getenv('PASS')

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

# Wait for page load
wait = WebDriverWait(driver, 30)

def facebook_login():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Log in")]'))).click()
    sleep(2)
    fb_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[text()="Log in with Facebook"]/..')))
    fb_btn.click()

    # Switch to Facebook popup
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    # Facebook login
    email_in = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_in.send_keys(FB_EMAIL)
    pass_in = driver.find_element(By.ID, "pass")
    pass_in.send_keys(FB_PASSWORD)
    pass_in.send_keys(Keys.ENTER)

    # Switch back to Tinder window
    sleep(5)
    driver.switch_to.window(driver.window_handles[0])

def dismiss_popups():
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Allow"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not interested"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]'))).click()
    except:
        pass
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Maybe Later"]'))).click()
    except:
        pass

def auto_swipe():
    while True:
        try:
            sleep(1)
            like_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Like"]')))
            like_btn.click()
        except:
            try:
                match_popup = driver.find_element(By.XPATH, '//button[contains(text(), "Back to Tinder")]')
                match_popup.click()
            except:
                sleep(2)

# Execute
facebook_login()
dismiss_popups()
auto_swipe()
