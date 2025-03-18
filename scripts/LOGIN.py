from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

options = Options()
options.add_argument("--incognito")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver,200)
confirmed = False

def log_in():
    with open("credentials.txt", "r") as file:
    	username = file.readline().strip()
    	password = file.readline().strip()
    driver.get("https://humanbenchmark.com/login")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'fc-button-label'))).click()
    confirmed = True
    print('found Confirm')
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.NAME,'username'))).send_keys(username, Keys.TAB, password, Keys.RETURN)
    print('Logged in')
    sleep(2)


