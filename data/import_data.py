import os
import django
import sys
import csv
from django.utils import timezone

# Thiết lập môi trường Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcooking.settings")  
django.setup()

import csv
import ast
from users.models import User
from recipes.models import Category, DetailCategory, Ingredient, Recipe, RecipeIngredient
from reviews.models import Review
from django.contrib.auth import get_user_model


def load_users():
    print("🔄 Đang import người dùng...")
    users = [
        {"username": "admin", "email": "admin@example.com", "password": "admin123", "is_admin": True},
        {"username": "user1", "email": "user1@example.com", "password": "user123", "is_admin": False},
        {"username": "user2", "email": "user2@example.com", "password": "user456", "is_admin": False},
    ]

    for u in users:
        user, created = User.objects.get_or_create(
            username=u["username"],
            email=u["email"],
            is_admin=u["is_admin"]
        )
        user.set_password(u["password"])  # mã hóa mật khẩu
        user.save()
        
    with open("data/users.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user, created = User.objects.get_or_create(
                username=row["username"],
                email=row["email"],
                is_admin=row["is_admin"].strip().lower() == "true"
            )
            user.set_password(row["password"])  
            user.save()

    print("✅ Đã import xong tất cả người dùng.")


def load_ingredients():
    print("🔄 Đang import nguyên liệu...")
    with open("data/recipe_ingredients.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        ingredient_names = {row["ingredient"].strip() for row in reader}
        for name in ingredient_names:
            Ingredient.objects.get_or_create(name=name)
    print("✅ Đã import xong nguyên liệu.")

def load_recipes():
    print("🔄 Đang import công thức...")

    User = get_user_model()
    try:
        admin_user = User.objects.get(username='admin')
    except User.DoesNotExist:
        return

    with open("data/recipes.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Recipe.objects.get_or_create(
                name=row["name"],
                defaults={
                    "description": row["description"],
                    "cook_time": int(row["cook_time"]) if row["cook_time"].isdigit() else None,
                    "instructions": row["instructions"],
                    "image": row["image_path"] if row["image_path"] else None,
                    "author": admin_user,
                }
            )

    print("✅ Đã import xong công thức.")

def load_recipe_ingredients():
    print("🔄 Đang import nguyên liệu cho từng công thức...")
    with open("data/recipe_ingredients.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                recipe = Recipe.objects.get(name=row["recipe"])
                ingredient = Ingredient.objects.get(name=row["ingredient"])
                RecipeIngredient.objects.get_or_create(
                    recipe=recipe,
                    ingredient=ingredient,
                    defaults={"quantity": row["quantity"]}
                )
            except Exception as e:
                print(f"❌ Lỗi khi thêm nguyên liệu cho công thức {row['recipe']}: {e}")
    print("✅ Đã import xong nguyên liệu cho công thức.")

def load_categories():
    print("🔄 Đang tạo danh mục món ăn...")
    categories = {
        "Theo bữa ăn": ["Bữa sáng", "Bữa trưa", "Bữa tối", "Bữa xế", "Ăn khuya"],
        "Theo vùng miền/quốc gia": ["Món Việt Nam", "Món Trung Quốc", "Món Nhật Bản", "Món Hàn Quốc", "Món Âu", "Món Mỹ", "Món Ấn Độ", "Món Địa Trung Hải"],
        "Theo phương pháp chế biến": ["Món luộc", "Món hấp", "Món chiên", "Món nướng", "Món xào", "Món kho/rim", "Món gỏi/salad", "Món lẩu"],
        "Theo đặc điểm dinh dưỡng": ["Món chay", "Món giàu protein", "Món ít carb/Keto", "Món ít calo", "Món giàu chất xơ"],
        "Theo hình thức ăn uống": ["Món ăn vặt", "Món tráng miệng", "Món ăn đường phố", "Món nhà hàng", "Món ăn nhanh"],
        "Theo dịp đặc biệt": ["Món ngày Tết", "Món Giáng Sinh", "Món đám cưới", "Món sinh nhật"],
        "Theo độ khó nấu": ["Món đơn giản", "Món trung bình", "Món phức tạp"]
    }
    for key, values in categories.items():
        category, _ = Category.objects.get_or_create(name=key)
        for value in values:
            DetailCategory.objects.get_or_create(name=value, category=category)
    print("✅ Đã thêm xong danh mục món ăn.")

def load_reviews():
    print("🔄 Đang import đánh giá...")
    with open("data/reviews.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                recipe = Recipe.objects.get(name=row["recipe"])

                # Chuyển chuỗi dictionary thành dict thật
                user_info = ast.literal_eval(row["user"])
                username = user_info["username"]

                user = User.objects.get(username=username)

                Review.objects.get_or_create(
                    recipe=recipe,
                    user=user,
                    defaults={
                        "rating": int(row["rating"]),
                        "comment": row["comment"]
                    }
                )
                print(f"✅ Đã thêm đánh giá cho {recipe.name} bởi {username}")
            except Exception as e:
                print(f"❌ Lỗi khi thêm người dùng: {e}")
    print("✅ Đã import xong đánh giá.")

import csv
from recipes.models import Recipe, DetailCategory

def assign_categories_to_recipes():
    categories_recipes = {}

    with open("data/categories_recipe.csv", newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipe_name = row['recipe'].strip()
            category_name = row['category'].strip()

            if recipe_name not in categories_recipes:
                categories_recipes[recipe_name] = []

            if category_name not in categories_recipes[recipe_name]:
                categories_recipes[recipe_name].append(category_name)

    # Liên kết công thức với danh mục
    for recipe_name, category_names in categories_recipes.items():
        try:
            recipe = Recipe.objects.get(name=recipe_name)            
            category_objects = [DetailCategory.objects.get(name=category_name) for category_name in category_names]
            recipe.category.set(category_objects)
            print(f"✅ Đã liên kết công thức '{recipe_name}' với các danh mục {', '.join(category_names)}")
        except Exception as e:
            print(f"❌ Lỗi khi liên kết công thức '{recipe_name}' với danh mục: {e}")

if __name__ == "__main__":
    print("Bắt đầu import dữ liệu từ các file CSV...")
    load_users()
    load_ingredients()
    load_categories()
    load_recipes()
    assign_categories_to_recipes()
    load_recipe_ingredients()
    load_reviews()
    print("Hoàn tất import toàn bộ dữ liệu!")

