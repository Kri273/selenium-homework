import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ühendab lehega ära
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2)

# vajutab add element nuppu...
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

# ...5 korda
for _ in range(5):
    add_button.click()
    time.sleep(1)

print("Lisatud 5 elementi.")

# kustutab nuppe
while True:
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    if not delete_buttons:
        break
    delete_buttons[0].click()
    print("Kustutatud üks element.")
    time.sleep(1)

print("Kõik elemendid kustutatud.")

input("Vajuta Enter, et brauser sulgeda...")
driver.quit()