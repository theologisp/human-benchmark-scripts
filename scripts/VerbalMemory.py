from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from LOGIN import *
import threading
import keyboard

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
        driver.get("https://humanbenchmark.com/tests/verbal-memory")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'css-de05nr'))).click()
        print('Started')
        sleep(3)
        
        seen_words = []
        
        while not stop_flag:
            word = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'word'))).text
            print(word)
            if word not in seen_words:
                seen_words.append(word)
                wait.until(EC.presence_of_element_located((By.XPATH,'//button[text()="NEW"]'))).click()
            else:
                wait.until(EC.presence_of_element_located((By.XPATH,'//button[text()="SEEN"]'))).click()
    except Exception as e:
        print (e, 'rekt')

open_hb()