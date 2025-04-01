# from .models import Category, Ingredient, Recipe, RecipeIngredient

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
#     {"name": "Đậu hũ chiên", "instructions": "Chiên giòn đậu hũ với dầu ăn.", "cook_time": 10, "category": mon_chay, "image": "recipe_images/dau_hu_chien.jpg"},
#     {"name": "Canh gà hầm sâm", "instructions": "Hầm gà với nhân sâm, táo đỏ, và gừng.", "cook_time": 60, "category": mon_man, "image": "recipe_images/canh_ga_ham_sam.jpg"},
#     {"name": "Bò lúc lắc", "instructions": "Xào thịt bò với ớt chuông và hành tây.", "cook_time": 20, "category": mon_man, "image": "recipe_images/bo_luc_lac.jpg"},
#     {"name": "Súp bí đỏ", "instructions": "Nấu bí đỏ với sữa tươi rồi xay nhuyễn.", "cook_time": 30, "category": mon_nuoc, "image": "recipe_images/sup_bi_do.jpg"},
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

# from users.models import User
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

# from reviews.models import Review

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