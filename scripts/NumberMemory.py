from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from LOGIN import *
import keyboard
import threading

stop_flag = False

def listen_for_escape():
    global stop_flag
    keyboard.wait('esc')
    stop_flag = True
    print("Failsafe triggered: ESC pressed.")

def open_hb():  
    threading.Thread(target=listen_for_escape, daemon=True).start()  
    try:
        log_in()
        driver.get("https://humanbenchmark.com/tests/number-memory")
        wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Start"]'))).click()
        print('found Start')
        sleep(1)
        while not stop_flag:
            sleep(0.5)
            big_number_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'big-number '))).text
            print('found number ' + big_number_text)
            input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1qvtbrk.e19owgy78 input')))
            input_field.send_keys(big_number_text)
            sleep(0.2)
            input_field.send_keys(Keys.RETURN)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="NEXT"]'))).click()
    except Exception as e:
        print (e, 'rekt')

open_hb()