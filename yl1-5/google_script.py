import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()   # leiab Chromedriveri PATH-ist

# ühendab lehega ära
driver.get("https://www.google.com")
time.sleep(2)

# acceptib cookies
try:
    accept_button = driver.find_element(By.XPATH, "//button[contains(., 'Accept')]")
    accept_button.click()
    print("Vajutasin: Accept")
except:
    try:
        reject_button = driver.find_element(By.XPATH, "//button[contains(., 'Reject')]")
        reject_button.click()
        print("Vajutasin: Reject")
    except:
        print("Küpsiste lehte ei ilmunud.")

time.sleep(2)

# lisab nime

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Kristelle Tasane")

input("Vajuta Enter, et brauser sulgeda...")