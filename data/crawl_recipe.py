import time
import csv
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import random
import selenium.common.exceptions

# Biến toàn cục
recipe_ingredients = []
reviews = []
categories_recipe = []
users = []

def load_users(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("username"):  
                    users.append(row)
        print(f"✅ Đã load {len(users)} user từ {file_path}")
    except Exception as e:
        print(f"❌ Lỗi khi đọc user từ file {file_path}: {e}")
    return users

# Danh sách phân loại có sẵn
categories = {
    "Theo bữa ăn": [
        "Bữa sáng",
        "Bữa trưa",
        "Bữa tối",
        "Bữa xế",
        "Ăn khuya"
    ],
    "Theo vùng miền/quốc gia": [
        "Món Việt Nam",
        "Món Trung Quốc",
        "Món Nhật Bản",
        "Món Hàn Quốc",
        "Món Âu",
        "Món Mỹ",
        "Món Ấn Độ",
        "Món Địa Trung Hải"
    ],
    "Theo phương pháp chế biến": [
        "Món luộc",
        "Món hấp",
        "Món chiên",
        "Món nướng",
        "Món xào",
        "Món kho/rim",
        "Món gỏi/salad",
        "Món lẩu"
    ],
    "Theo đặc điểm dinh dưỡng": [
        "Món chay",
        "Món giàu protein",
        "Món ít carb/Keto",
        "Món ít calo",
        "Món giàu chất xơ"
    ],
    "Theo hình thức ăn uống": [
        "Món ăn vặt",
        "Món tráng miệng",
        "Món ăn đường phố",
        "Món nhà hàng",
        "Món ăn nhanh"
    ],
    "Theo dịp đặc biệt": [
        "Món ngày Tết",
        "Món Giáng Sinh",
        "Món đám cưới",
        "Món sinh nhật"
    ],
    "Theo độ khó nấu": [
        "Món đơn giản",
        "Món trung bình",
        "Món phức tạp"
    ]
}

# Hàm tách nguyên liệu và số lượng
def parse_ingredient(ingredient_text):
    """Tách nguyên liệu và số lượng từ văn bản, phân tách tại chữ số đầu tiên hoặc dấu hai chấm (nếu trước số), bỏ qua 'ĂN KÈM', bỏ dấu hai chấm."""
    ingredient_text = ingredient_text.strip()
    
    if not ingredient_text or ingredient_text.startswith("ĂN KÈM"):
        return None
    
    # Tìm chữ số đầu tiên hoặc dấu hai chấm
    number_pattern = r'\b\d'  
    colon_pattern = r':'
    
    # Tìm vị trí của chữ số và dấu hai chấm
    number_match = re.search(number_pattern, ingredient_text)
    colon_match = re.search(colon_pattern, ingredient_text)
    
    # Xác định điểm phân tách (chữ số hoặc dấu hai chấm, lấy cái xuất hiện đầu tiên)
    split_pos = None
    if number_match and colon_match:
        split_pos = min(number_match.start(), colon_match.start())
    elif number_match:
        split_pos = number_match.start()
    elif colon_match:
        split_pos = colon_match.start()
    
    if split_pos is not None:
        ingredient = ingredient_text[:split_pos].strip()
        quantity = ingredient_text[split_pos:].strip()

        ingredient = ingredient.replace(":", "").strip()
        quantity = quantity.replace(":", "").strip()
    else:
        ingredient = ingredient_text.replace(":", "").strip()
        quantity = ""
    
    if not ingredient:
        return None
        
    return ingredient, quantity

# Hàm tải hình ảnh
def download_image(driver, recipe_url, output_dir):
    """Tải hình ảnh từ URL của công thức và lưu vào thư mục chỉ định."""
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.img_detail_monan"))
        )

        image_element = driver.find_element(By.CSS_SELECTOR, "img.img_detail_monan")
        image_url = image_element.get_attribute("src")
        image_name = image_element.get_attribute("alt").replace(" ", "_").replace("/", "_") + ".jpg"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Tải hình ảnh và lưu vào tệp
        response = requests.get(image_url)
        if response.status_code == 200:
            image_path = os.path.join(output_dir, image_name).replace("\\", "/")
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"✅ Hình ảnh đã được lưu tại: {image_path}")
            return image_path
        else:
            print(f"❌ Không thể tải hình ảnh, mã phản hồi: {response.status_code}")
    except Exception as e:
        print(f"❌ Lỗi khi tải hình ảnh từ {recipe_url}: {e}")
    
    return None

# Lấy tất cả các bước Sơ Chế, Thực Hiện, và Cách Dùng và gộp lại thành một instruction
def crawl_all_instructions(driver):
    """Cào các bước từ các section Sơ Chế, Thực Hiện, Cách Dùng với cấu trúc HTML khác nhau."""
    try:
        instructions = []

        # Sơ Chế: Kiểm tra cả <ul><li> và <div class="ewa-rteLine">
        soche_elements = []

        try:
            soche_elements = driver.find_elements(By.CSS_SELECTOR, "#section-soche ul li")
        except:
            pass

        try:
            soche_elements += driver.find_elements(By.CSS_SELECTOR, "#section-soche div.ewa-rteLine")
        except:
            pass

        if not soche_elements:
            try:
                soche_elements += driver.find_elements(By.CSS_SELECTOR, "#section-soche p")
            except:
                pass

        instructions.extend([element.text.strip() for element in soche_elements if element.text.strip().lstrip()])

        # Thực Hiện: Kiểm tra cả <div><p> và <div class="ewa-rteLine">
        thuchien_elements = []
        try:
            thuchien_elements = driver.find_elements(By.CSS_SELECTOR, "#section-thuchien div p")
        except:
            pass
        try:
            thuchien_elements += driver.find_elements(By.CSS_SELECTOR, "#section-thuchien div.ewa-rteLine")
        except:
            pass
        if not thuchien_elements:
            try:
                thuchien_elements += driver.find_elements(By.CSS_SELECTOR, "#section-soche p")
            except:
                pass
        instructions.extend([element.text.strip() for element in thuchien_elements if element.text.strip().lstrip()])

        # Cách Dùng: Kiểm tra cả <div><p> và <div class="ewa-rteLine">
        cachdung_elements = []
        try:
            cachdung_elements = driver.find_elements(By.CSS_SELECTOR, "#section-howtouse div p")
        except:
            pass
        try:
            cachdung_elements += driver.find_elements(By.CSS_SELECTOR, "#section-howtouse div.ewa-rteLine")
        except:
            pass
        if not cachdung_elements:
            try:
                cachdung_elements += driver.find_elements(By.CSS_SELECTOR, "#section-soche p")
            except:
                pass
        instructions.extend([element.text.strip() for element in cachdung_elements if element.text.strip().lstrip()])

        # Gộp tất cả các bước lại thành một chuỗi
        return "\n".join(instructions) if instructions else None
    except Exception as e:
        print(f"❌ Lỗi khi cào các bước: {e}")
        return None

# Cào phân loại từ công thức
def crawl_categories(recipe_name, driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.tags > li > a"))
        )
        category_elements = driver.find_elements(By.CSS_SELECTOR, "ul.tags > li > a")
        crawled_categories = [element.text.strip() for element in category_elements]
        for group, valid_categories in categories.items():
            for crawled_category in crawled_categories:
                if crawled_category in valid_categories:
                    categories_recipe.append({
                        "recipe": recipe_name,
                        "category": crawled_category
                    })
    except Exception as e:
        print(f"❌ Lỗi khi cào phân loại: {e}")

# Cào chi tiết công thức
def crawl_recipe_details(url, driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1 span.title"))
        )
    except Exception as e:
        print(f"❌ Không thể load chi tiết từ {url}: {e}")
        return None

    try:
        name = driver.find_element(By.CSS_SELECTOR, "h1 span.title").text.strip()

        # Hình ảnh
        image_path = download_image(driver, url, "media/recipe_images").replace("media/", "")

        # Mô tả
        description_elements = driver.find_elements(By.CSS_SELECTOR, ".detail_main > div > p")
        description = ""
        if description_elements:
            description_parts = []
            for element in description_elements:
                text = element.text.strip()
                if not text.startswith("Xem thêm"):
                    description_parts.append(text)
            description = "\n".join(description_parts) if description_parts else ""

        # Thời gian nấu
        cook_time = None
        try:
            cook_time_element = driver.find_element(By.XPATH, "//span[text()='Thời gian thực hiện:']/following-sibling::strong")
            cook_time_text = cook_time_element.text.strip()
            cook_time = int(re.search(r'\d+', cook_time_text).group()) if cook_time_text else None
        except:
            pass

        # Độ khó
        level = "Không rõ"
        try:
            level_element = driver.find_element(By.XPATH, "//span[text()='Độ khó:']/following-sibling::strong")
            level = level_element.text.strip()
        except:
            pass

        # Cào nguyên liệu
        ingredients_elements = driver.find_elements(By.CSS_SELECTOR, "#tab-muong ul li:not(.giavi)")
        for element in ingredients_elements:
            ingredient_text = element.text.strip()
            if ingredient_text:  # Chỉ xử lý nếu không rỗng
                parsed_ingredient = parse_ingredient(ingredient_text)
                if parsed_ingredient:  # Chỉ thêm nếu không phải "ĂN KÈM" hoặc không hợp lệ
                    ingredient, quantity = parsed_ingredient
                    recipe_ingredients.append({
                        "recipe": name,
                        "ingredient": ingredient,
                        "quantity": quantity
                    })
                else:
                    print(f"⚠️ Bỏ qua nguyên liệu không hợp lệ: '{ingredient_text}'")

        # Hướng dẫn
        instructions = crawl_all_instructions(driver)

        # Cào phân loại
        crawl_categories(name, driver)

        # Cào comment của người xem 
        try:
            comment_elements = driver.find_elements(By.CSS_SELECTOR, ".list-all-comment > div")
            for comment in comment_elements:
                try:
                    username = comment.find_element(By.CSS_SELECTOR, "div > div > div > strong").text.strip()
                    if username != "Món Ngon Mỗi Ngày":
                        comment_text = comment.find_element(By.CSS_SELECTOR, "p:not(.text-xs)").text.strip()
                        if comment_text:
                            reviews.append({
                                "recipe": name,
                                "user": random.choice(users),
                                "rating": random.randint(1, 5), 
                                "comment": comment_text
                            })
                except:
                    continue
        except:
            pass

        return {
            "name": name,
            "description": description,
            "cook_time": cook_time,
            "level": level,
            "instructions": instructions,
            "image_path": image_path
        }
    except Exception as e:
        print(f"❌ Lỗi khi cào dữ liệu từ {url}: {e}")
        return None

# Cào danh sách công thức
def crawl_all_recipes(start_page_url, max_pages):
    """Cào tất cả công thức từ các trang."""
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)

    all_recipes = []
    page = 1

    try:
        while page <= max_pages:
            page_url = f"{start_page_url}/page/{page}/"
            print(f"🔄 Đang cào trang {page}: {page_url}")
            driver.get(page_url)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3.font-bold > a"))
                )
            except:
                print("❌ Không có thêm link nào, dừng lại.")
                break

            try:
                link_elements = driver.find_elements(By.CSS_SELECTOR, "h3.font-bold > a")
                recipe_urls = [el.get_attribute("href") for el in link_elements if el.get_attribute("href")]

                if not recipe_urls:
                    print("❌ Không tìm thấy link nào.")
                    break

                for recipe_url in recipe_urls:
                    try:
                        print(f"➡️ Cào dữ liệu từ: {recipe_url}")
                        recipe_data = crawl_recipe_details(recipe_url, driver)
                        if recipe_data:
                            all_recipes.append(recipe_data)
                    except selenium.common.exceptions.StaleElementReferenceException:
                        print("⚠️ Lỗi StaleElementReferenceException: Bỏ qua liên kết đã stale.")
                        continue
                    except Exception as e:
                        print(f"❌ Lỗi khác khi xử lý liên kết {recipe_url}: {e}")
                        continue

            except selenium.common.exceptions.StaleElementReferenceException:
                print("⚠️ Lỗi StaleElementReferenceException khi lấy danh sách liên kết, thử lại trang.")
                continue

            page += 1
            time.sleep(random.uniform(1, 3)) 
    finally:
        driver.quit()

    return all_recipes


# Lưu dữ liệu vào CSV
def save_to_csv(data, filename, fieldnames):
    with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Đã lưu dữ liệu vào: {filename}")

# Main
if __name__ == "__main__":
    users = load_users("data/users.csv")
    
    start_url = "https://monngonmoingay.com/tim-kiem-mon-ngon"
    recipes = crawl_all_recipes(start_url, max_pages=198)

    save_to_csv(recipes, "data/recipes.csv", ["name", "description", "cook_time", "level", "instructions", "image_path"])
    save_to_csv(recipe_ingredients, "data/recipe_ingredients.csv", ["recipe", "ingredient", "quantity"])
    save_to_csv(reviews, "data/reviews.csv", ["recipe", "user", "rating", "comment"])
    save_to_csv(categories_recipe, "data/categories_recipe.csv", ["recipe", "category"])

    # Lưu danh sách nguyên liệu vào ingredients.csv
    unique_ingredients = [{"ingredient": item} for item in sorted({ri["ingredient"] for ri in recipe_ingredients})]
    save_to_csv(unique_ingredients, "data/ingredients.csv", ["ingredient"])

    print("✅ Dữ liệu đã được lưu thành công!")