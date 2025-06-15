from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import os

options = Options()
options.add_argument("--incognito")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver,200)
confirmed = False

def log_in():
    # include your login credentials in the file scripts/credentials.txt if you want to login
    # it will continue otherwise 
    cred_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "credentials.txt"))
    with open(cred_path, "r") as file:
        username = file.readline().strip()
        password = file.readline().strip()
    driver.get("https://www.humanbenchmark.com/login")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'fc-button-label'))).click()
    print('found Confirm')
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys(username, Keys.TAB, password, Keys.RETURN)
    print('Logged in')
    sleep(2)


