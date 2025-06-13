from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from LOGIN import *

def open_hb():    
    try:
        log_in()
        driver.get("https://humanbenchmark.com/tests/typing")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'incomplete')))
        print('Starting')
        sleep(3)
        text = []
        elements = driver.find_elements(By.CLASS_NAME, 'incomplete')
        
        for i in range(len(elements)):
            if elements[i].text == '':
                text.append(' ')
            else:
                text.append(elements[i].text)
            
        new = ''.join(text)
        print(new)

        input = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'notranslate')))
        input.send_keys(new)
    except Exception as e:
        print (e, 'rekt')

open_hb()
