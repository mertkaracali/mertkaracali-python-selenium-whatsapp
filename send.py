from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import autoit
import argparse

parser = argparse.ArgumentParser(description="Just an example",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--number", type=int, help="Number")
parser.add_argument("-m", "--message", type=str, help="Message")
args = parser.parse_args()

def get_random_message(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        messages = file.readlines()
    return random.choice(messages).strip()

def send_message(phone_number, message):
    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
    message_box = driver.find_element(By.XPATH, message_box_xpath)
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
phone_number = args.number #Mesaj göndermek istediğin telefon numarasını gir.
chrome_options = Options()
chrome_options.add_argument("user-data-dir=/data");#Cacheee
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
driver.get("https://web.whatsapp.com/send?phone=" + str(phone_number))
time.sleep(20)


send_message(phone_number, str(args.message))
print("true")


time.sleep(1)
driver.quit()



