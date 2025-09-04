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

# kontrolli, kas õnnestus
try:
    success_message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in success_message:
        print("TEST ÕNNESTUS")
    else:
        print("TEST EBAÕNNESTUS")
except Exception as e:
    print("TEST EBAÕNNESTUS")
    print(str(e))


input("Vajuta Enter, et brauser sulgeda...")
driver.quit()
