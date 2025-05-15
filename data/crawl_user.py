import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)

url = 'https://www.threads.com/@embelem._/post/DHSNRJASC_w'  
driver.get(url)

time.sleep(5)

elements = driver.find_elements(By.TAG_NAME, "a")

usernames = set()
target_username = url.split("/@")[1]
for el in elements:
    href = el.get_attribute("href")
    if href and "/@" in href:
        try:
            part = href.split("/@")[1]
            username = part.split("/")[0]
            if username != target_username:
                usernames.add(username)
        except IndexError:
            continue

users = []
for username in usernames:
    user = {
        "username": username,
        "email": f"{username}@example.com",
        "password": "abc123",
        "is_admin": False
    }
    users.append(user)

with open("data/users.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["username", "email", "password", "is_admin"])
    writer.writeheader()
    writer.writerows(users)

print(f"Đã lưu {len(users)} user vào 'users.csv'.")

driver.quit()