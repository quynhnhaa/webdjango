from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import defaultdict
import json

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
driver.maximize_window()

categories = defaultdict(list)

try:
    driver.get("https://monngonmoingay.com/tim-kiem-mon-ngon/")
    driver.implicitly_wait(10)

    # Đóng popup cookie nếu có
    try:
        accept_cookie_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookieDrawer__acceptAll"))
        )
        accept_cookie_btn.click()
        time.sleep(1)
    except:
        print("Không tìm thấy popup cookie, tiếp tục...")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "advanced-group"))
    )

    # Tìm các accordion
    accordion_buttons = driver.find_elements(By.XPATH, "//button[.//span[contains(@class, 'icon icon-[ph--caret-down-fill]')]]")

    for button in accordion_buttons:
        try:
            category_name = driver.execute_script("return arguments[0].innerText;", button).strip()

            # Bỏ qua danh mục "Ajinomoto" và các mục con của nó
            if "Sản phẩm Ajinomoto" in category_name:
                continue

        except Exception as e:
            print("Lỗi:", e)
            continue

        accordion_body_id = button.get_attribute("aria-controls")

        # Click để mở accordion
        driver.execute_script("arguments[0].click();", button)

        try:
            accordion_body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, accordion_body_id))
            )
        except Exception as e:
            print(f"Không tìm thấy nội dung accordion (ID={accordion_body_id}): {str(e)}")
            continue

        subcategory_elements = accordion_body.find_elements(By.CSS_SELECTOR, "label")

        for elem in subcategory_elements:
            try:
                span_elem = elem.find_element(By.CSS_SELECTOR, "span")
                label = driver.execute_script("return arguments[0].innerText;", span_elem).strip()

                # Bỏ qua nhãn chứa "khác" và "ajinomoto"
                if label and "khác" not in label.lower() :
                    categories[category_name].append(label)
            except Exception as e:
                print("Lỗi:", e)
                continue

finally:
    driver.quit()

# ✅ Thêm mục "Khác" vào cuối
categories["Khác"] = ["Khác"]

# Lưu vào file
output_file = "data/categories.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(categories, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu danh mục vào {output_file}")

# Hiển thị kết quả
from pprint import pprint
pprint(dict(categories))
