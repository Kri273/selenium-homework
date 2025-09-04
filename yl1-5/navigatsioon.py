import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ühendab lehega ära
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

# vajutab vajalikule lingile
link = driver.find_element(By.LINK_TEXT, "Checkboxes")
link.click()
time.sleep(1)


# leiab ja vajutab checkboxile
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for cb in checkboxes:
    if not cb.is_selected():
        cb.click()

time.sleep(1)
# läheb tagasi
driver.back()


input("Vajuta Enter, et brauser sulgeda...")
driver.quit()