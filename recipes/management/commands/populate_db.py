# import json
# from ...models import Category, Ingredient, Recipe, RecipeIngredient
# from users.models import User
# from reviews.models import Review

# categories = ["Món chay", "Món mặn", "Món tráng miệng", "Món nước", "Món nướng"]
# for name in categories:
#     Category.objects.get_or_create(name=name)
# print("Danh mục món ăn đã được thêm vào.")

# ingredients = ["Thịt gà", "Thịt bò", "Đậu hũ", "Cà rốt", "Khoai tây", "Hành tím", "Tỏi", "Gừng", "Sữa đặc", "Bột mì"]
# for name in ingredients:
#     Ingredient.objects.get_or_create(name=name)
# print("Nguyên liệu đã được thêm vào.")

# mon_chay = Category.objects.get(name="Món chay")
# mon_man = Category.objects.get(name="Món mặn")
# mon_nuoc = Category.objects.get(name="Món nước")

# recipes = [
#     {"name": "Đậu hũ chiên", "instructions": json.dumps([
#         {"step": 1, "instruction": "Cắt đậu hũ thành miếng nhỏ."},
#         {"step": 2, "instruction": "Chiên giòn đậu hũ với dầu ăn."}
#     ]), "cook_time": 10, "category": mon_chay, "image": "recipe_images/dau_hu_chien.jpg"},
#     {"name": "Canh gà hầm sâm", "instructions": json.dumps([
#         {"step": 1, "instruction": "Hầm gà với nhân sâm, táo đỏ, và gừng."}
#     ]), "cook_time": 60, "category": mon_man, "image": "recipe_images/canh_ga_ham_sam.jpg"},
#     {"name": "Bò lúc lắc", "instructions": json.dumps([
#         {"step": 1, "instruction": "Xào thịt bò với ớt chuông và hành tây."}
#     ]), "cook_time": 20, "category": mon_man, "image": "recipe_images/bo_luc_lac.jpg"},
#     {"name": "Súp bí đỏ", "instructions": json.dumps([
#         {"step": 1, "instruction": "Nấu bí đỏ với sữa tươi rồi xay nhuyễn."}
#     ]), "cook_time": 30, "category": mon_nuoc, "image": "recipe_images/sup_bi_do.jpg"},
# ]

# for r in recipes:
#     Recipe.objects.get_or_create(name=r["name"], defaults=r)
# print("Món ăn đã được thêm vào.")

# recipe_ingredients = [
#     {"recipe": "Đậu hũ chiên", "ingredient": "Đậu hũ", "quantity": "200g"},
#     {"recipe": "Canh gà hầm sâm", "ingredient": "Thịt gà", "quantity": "1 con"},
#     {"recipe": "Canh gà hầm sâm", "ingredient": "Gừng", "quantity": "1 nhánh"},
#     {"recipe": "Bò lúc lắc", "ingredient": "Thịt bò", "quantity": "300g"},
#     {"recipe": "Súp bí đỏ", "ingredient": "Khoai tây", "quantity": "200g"},
# ]

# for ri in recipe_ingredients:
#     recipe = Recipe.objects.get(name=ri["recipe"])
#     ingredient = Ingredient.objects.get(name=ri["ingredient"])
#     RecipeIngredient.objects.get_or_create(recipe=recipe, ingredient=ingredient, quantity=ri["quantity"])
# print("Nguyên liệu đã được gán vào món ăn.")

# users = [
#     {"username": "admin", "email": "admin@example.com", "password": "admin123", "is_admin": True},
#     {"username": "user1", "email": "user1@example.com", "password": "user123", "is_admin": False},
#     {"username": "user2", "email": "user2@example.com", "password": "user456", "is_admin": False},
# ]

# for u in users:
#     user, created = User.objects.get_or_create(username=u["username"], email=u["email"], is_admin=u["is_admin"])
#     user.set_password(u["password"])  # Mã hóa mật khẩu
#     user.save()
# print("Người dùng đã được thêm vào.")

# reviews = [
#     {"recipe": "Đậu hũ chiên", "user": "user1", "rating": 5, "comment": "Món ăn rất ngon!"},
#     {"recipe": "Canh gà hầm sâm", "user": "user2", "rating": 4, "comment": "Hầm lâu quá, nhưng hương vị tuyệt vời!"},
#     {"recipe": "Bò lúc lắc", "user": "user1", "rating": 3, "comment": "Bò hơi dai."},
# ]

# for r in reviews:
#     recipe = Recipe.objects.get(name=r["recipe"])
#     user = User.objects.get(username=r["user"])
#     Review.objects.create(recipe=recipe, user=user, rating=r["rating"], comment=r["comment"])
# print("Đánh giá món ăn đã được thêm vào.")

# # from ...models import Category, Ingredient, Recipe, RecipeIngredient

# # # Lấy danh mục "Món nước"
# # mon_nuoc = Category.objects.get(name="Món nước")

# # # Tạo công thức
# # recipe_data = {
# #     "name": "Bún bò Huế",
# #     "instructions": "Ngâm xương bò, chuẩn bị nước mắm ruốc, làm sa tế tôm, chần và nấu thịt bò và chân giò, ướp thịt bắp bò, làm hỗn hợp dầu, hoàn thiện món súp.",
# #     "cook_time": 300,
# #     "category": mon_nuoc,
# #     "image": "https://cookpad.com/vn/step_attachment/images/1d14a84890d46ec3?image_region_id=24",
# # }

# # Recipe.objects.get_or_create(name=recipe_data["name"], defaults=recipe_data)

# # # Thêm các nguyên liệu mới nếu chưa tồn tại
# # new_ingredients = [
# #     "xương bò",
# #     "chân giò",
# #     "mắm ruốc",
# #     "dầu ăn",
# #     "sả",
# #     "ớt bột",
# #     "ớt tươi",
# #     "đường",
# #     "muối",
# #     "dầu điều",
# #     "nước mắm",
# #     "bột tỏi",
# #     "bột điều đỏ",
# # ]

# # for name in new_ingredients:
# #     Ingredient.objects.get_or_create(name=name)

# # # Liên kết công thức với nguyên liệu
# # recipe_ingredients_data = [
# #     {"recipe": "Bún bò Huế", "ingredient": "xương bò", "quantity": "1.5 kg"},
# #     {"recipe": "Bún bò Huế", "ingredient": "thịt bò", "quantity": "1.5 kg"},
# #     {"recipe": "Bún bò Huế", "ingredient": "chân giò", "quantity": "1 kg"},
# #     {"recipe": "Bún bò Huế", "ingredient": "mắm ruốc", "quantity": "3 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "dầu ăn", "quantity": "5 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "tỏi", "quantity": "20 g"},
# #     {"recipe": "Bún bò Huế", "ingredient": "sả", "quantity": "150 g"},
# #     {"recipe": "Bún bò Huế", "ingredient": "hành tím", "quantity": "100 g"},
# #     {"recipe": "Bún bò Huế", "ingredient": "ớt bột", "quantity": "50 g"},
# #     {"recipe": "Bún bò Huế", "ingredient": "ớt tươi", "quantity": "100 g"},
# #     {"recipe": "Bún bò Huế", "ingredient": "đường", "quantity": "1 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "muối", "quantity": "1 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "dầu điều", "quantity": "1 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "nước mắm", "quantity": "2 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "bột tỏi", "quantity": "0.5 tbsp"},
# #     {"recipe": "Bún bò Huế", "ingredient": "bột điều đỏ", "quantity": "35 g"},
# # ]

# # for ri in recipe_ingredients_data:
# #     recipe = Recipe.objects.get(name=ri["recipe"])
# #     ingredient = Ingredient.objects.get(name=ri["ingredient"])
# #     RecipeIngredient.objects.get_or_create(recipe=recipe, ingredient=ingredient, quantity=ri["quantity"])

# # print("Công thức và nguyên liệu đã được thêm thành công.")

import json
from ...models import Category, Ingredient, Recipe, RecipeIngredient
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

categories = ["Món chay", "Món mặn", "Món tráng miệng", "Món nước", "Món nướng"]
for name in categories:
    Category.objects.get_or_create(name=name)
print("Danh mục món ăn đã được thêm vào.")

ingredients = ["Thịt gà", "Thịt bò", "Đậu hũ", "Cà rốt", "Khoai tây", "Hành tím", "Tỏi", "Gừng", "Sữa đặc", "Bột mì"]
for name in ingredients:
    Ingredient.objects.get_or_create(name=name)
print("Nguyên liệu đã được thêm vào.")

mon_chay = Category.objects.get(name="Món chay")
mon_man = Category.objects.get(name="Món mặn")
mon_nuoc = Category.objects.get(name="Món nước")

admin_user = User.objects.get(username="admin")  # Lấy admin làm người tạo

recipes = [
    {"name": "Đậu hũ chiên", "instructions": json.dumps([
        {"step": 1, "instruction": "Cắt đậu hũ thành miếng nhỏ."},
        {"step": 2, "instruction": "Chiên giòn đậu hũ với dầu ăn."}
    ]), "description": "Miếng đậu hũ mềm mịn bên trong, giòn rụm bên ngoài, thường được chiên vàng đều và dùng kèm với nước chấm chua ngọt hoặc mắm tỏi",
    "cook_time": 10, "category": mon_chay, "image": "recipe_images/dau_hu_chien.jpg", "author": admin_user},
    
    {"name": "Canh gà hầm sâm", "instructions": json.dumps([
        {"step": 1, "instruction": "Hầm gà với nhân sâm, táo đỏ, và gừng."}
    ]),  "description": "Món ăn bổ dưỡng kết hợp giữa thịt gà thơm mềm và nhân sâm, hầm chung với các loại thảo dược, tạo nên nước dùng thanh, bổ và giàu dinh dưỡng.",
    "cook_time": 60, "category": mon_man, "image": "recipe_images/canh_ga_ham_sam.jpg", "author": admin_user},
    
    {"name": "Bò lúc lắc", "instructions": json.dumps([
        {"step": 1, "instruction": "Xào thịt bò với ớt chuông và hành tây."}
    ]), "description":"Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.",
    "cook_time": 20, "category": mon_man, "image": "recipe_images/bo_luc_lac.jpg", "author": admin_user},
    
    {"name": "Súp bí đỏ", "instructions": json.dumps([
        {"step": 1, "instruction": "Nấu bí đỏ với sữa tươi rồi xay nhuyễn."}
    ]), "description": "Thịt bò mềm, đậm đà gia vị, được xào chín tới cùng rau củ như ớt chuông và hành tây, mang hương vị thơm ngon và cân bằng.", 
    "cook_time": 30, "category": mon_nuoc, "image": "recipe_images/sup_bi_do.jpg", "author": admin_user},
]

for r in recipes:
    Recipe.objects.get_or_create(name=r["name"], defaults=r)
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
