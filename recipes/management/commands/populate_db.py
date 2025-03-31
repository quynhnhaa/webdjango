import json
from ...models import Category, Ingredient, Recipe, RecipeIngredient, DetailCategory
from users.models import User
from reviews.models import Review

users = [
    {"username": "admin", "email": "admin@example.com", "password": "admin123", "is_admin": True},
    {"username": "user1", "email": "user1@example.com", "password": "user123", "is_admin": False},
    {"username": "user2", "email": "user2@example.com", "password": "user456", "is_admin": False},
]

for u in users:
    user, created = User.objects.get_or_create(username=u["username"], email=u["email"], is_admin=u["is_admin"])
    user.set_password(u["password"])  # Mã hóa mật khẩu
    user.save()
print("Người dùng đã được thêm vào.")

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
for key, values in categories.items():
    category, _ = Category.objects.get_or_create(name=key)
    for value in values:
        detail_category = DetailCategory.objects.get_or_create(name=value, category=category)
print("Danh mục món ăn đã được thêm vào.")

ingredients = ["Thịt gà", "Thịt bò", "Đậu hũ", "Cà rốt", "Khoai tây", "Hành tím", "Tỏi", "Gừng", "Sữa đặc", "Bột mì"]
for name in ingredients:
    Ingredient.objects.get_or_create(name=name)
print("Nguyên liệu đã được thêm vào.")

admin_user = User.objects.get(username="admin")  # Lấy admin làm người tạo

recipes = [
    {"name": "Đậu hũ chiên", "instructions": json.dumps([
        {"step": 1, "instruction": "Cắt đậu hũ thành miếng nhỏ."},
        {"step": 2, "instruction": "Chiên giòn đậu hũ với dầu ăn."}
    ]), "description": "Miếng đậu hũ mềm mịn bên trong, giòn rụm bên ngoài, thường được chiên vàng đều và dùng kèm với nước chấm chua ngọt hoặc mắm tỏi",
    "cook_time": 10, "image": "recipe_images/dau_hu_chien.jpg", "author": admin_user},
    
    {"name": "Canh gà hầm sâm", "instructions": json.dumps([
        {"step": 1, "instruction": "Hầm gà với nhân sâm, táo đỏ, và gừng."}
    ]),  "description": "Món ăn bổ dưỡng kết hợp giữa thịt gà thơm mềm và nhân sâm, hầm chung với các loại thảo dược, tạo nên nước dùng thanh, bổ và giàu dinh dưỡng.",
    "cook_time": 60, "image": "recipe_images/canh_ga_ham_sam.jpg", "author": admin_user},
    
    {"name": "Bò lúc lắc", "instructions": json.dumps([
        {"step": 1, "instruction": "Xào thịt bò với ớt chuông và hành tây."}
    ]), "description":"Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.",
    "cook_time": 20, "image": "recipe_images/bo_luc_lac.jpg", "author": admin_user},
    
    {"name": "Súp bí đỏ", "instructions": json.dumps([
        {"step": 1, "instruction": "Nấu bí đỏ với sữa tươi rồi xay nhuyễn."}
    ]), "description": "Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.", 
    "cook_time": 30, "image": "recipe_images/sup_bi_do.jpg", "author": admin_user},
]

for i, r in enumerate(recipes):
    created, _ = Recipe.objects.get_or_create(name=r["name"], defaults=r)
    created.category.set([i + 1])
print("Món ăn đã được thêm vào.")

recipe_ingredients = [
    {"recipe": "Đậu hũ chiên", "ingredient": "Đậu hũ", "quantity": "200g"},
    {"recipe": "Canh gà hầm sâm", "ingredient": "Thịt gà", "quantity": "1 con"},
    {"recipe": "Canh gà hầm sâm", "ingredient": "Gừng", "quantity": "1 nhánh"},
    {"recipe": "Bò lúc lắc", "ingredient": "Thịt bò", "quantity": "300g"},
    {"recipe": "Súp bí đỏ", "ingredient": "Khoai tây", "quantity": "200g"},
]

for ri in recipe_ingredients:
    recipe = Recipe.objects.get(name=ri["recipe"])
    ingredient = Ingredient.objects.get(name=ri["ingredient"])
    RecipeIngredient.objects.get_or_create(recipe=recipe, ingredient=ingredient, quantity=ri["quantity"])
print("Nguyên liệu đã được gán vào món ăn.")



reviews = [
    {"recipe": "Đậu hũ chiên", "user": "user1", "rating": 5, "comment": "Món ăn rất ngon!"},
    {"recipe": "Canh gà hầm sâm", "user": "user2", "rating": 4, "comment": "Hầm lâu quá, nhưng hương vị tuyệt vời!"},
    {"recipe": "Bò lúc lắc", "user": "user1", "rating": 3, "comment": "Bò hơi dai."},
]

for r in reviews:
    recipe = Recipe.objects.get(name=r["recipe"])
    user = User.objects.get(username=r["user"])
    Review.objects.create(recipe=recipe, user=user, rating=r["rating"], comment=r["comment"])
print("Đánh giá món ăn đã được thêm vào.")
