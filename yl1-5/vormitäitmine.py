import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ühendab lehega ära
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# kasutajanimi
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# parool
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# login nupp
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

input("Vajuta Enter, et brauser sulgeda...")
driver.quit()
