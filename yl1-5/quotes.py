import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ühendab lehega ära
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
time.sleep(2)

# otsib teksti ja autori
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

# prindib need terminali
for i in range(len(quotes)):
    print(f"{quotes[i].text} — {authors[i].text}")

input("Vajuta Enter, et brauser sulgeda...")
