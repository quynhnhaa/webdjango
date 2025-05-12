import json
from users.models import User
from recipes.models import Category, DetailCategory, Ingredient, Recipe, RecipeIngredient


# 1. Tạo người dùng
users = [
    {"username": "admin", "email": "admin@example.com", "password": "admin123", "is_admin": True},
    {"username": "user1", "email": "user1@example.com", "password": "user123", "is_admin": False},
    {"username": "user2", "email": "user2@example.com", "password": "user456", "is_admin": False},
    {"username": "chef1", "email": "chef1@example.com", "password": "chef123", "is_admin": False},
]
for u in users:
    user, created = User.objects.get_or_create(
        username=u["username"],
        email=u["email"],
        defaults={"is_admin": u["is_admin"]}
    )
    if created:
        user.set_password(u["password"])
        user.save()
print("Đã thêm người dùng.")

# 2. Tạo danh mục (Category) và chi tiết danh mục (DetailCategory)
categories = {
    "Theo bữa ăn": [
        "Bữa sáng", "Bữa trưa", "Bữa tối", "Bữa xế", "Ăn khuya"
    ],
    "Theo vùng miền/quốc gia": [
        "Món Việt Nam", "Món Trung Quốc", "Món Nhật Bản", "Món Hàn Quốc", "Món Âu",
        "Món Thái", "Món Ấn Độ"
    ],
    "Theo phương pháp chế biến": [
        "Món luộc", "Món hấp", "Món chiên", "Món nướng", "Món xào",
        "Món kho", "Món soup"
    ],
    "Theo đặc điểm dinh dưỡng": [
        "Món chay", "Món giàu protein", "Món ít carb/Keto", "Món ít calo",
        "Món giàu chất xơ"
    ],
    "Theo dịp đặc biệt": [
        "Món ngày Tết", "Món Giáng Sinh", "Món sinh nhật"
    ],
}
for cat_name, details in categories.items():
    category, _ = Category.objects.get_or_create(name=cat_name)
    for detail_name in details:
        DetailCategory.objects.get_or_create(name=detail_name, category=category)
print("Đã thêm danh mục và chi tiết danh mục.")

ingredients = ["Thịt gà", "Thịt bò", "Đậu hũ", "Cà rốt", "Khoai tây", "Hành tím", "Tỏi", "Gừng", "Sữa đặc", "Bột mì",
    "Cua thịt", "Mỳ Ý", "Bơ lạt", "Sốt cà chua đậm đặc", "Hành tỏi băm", "Nước luộc mì", "Lá oregano",
    "Whipping cream", "Phô mai parmesan", "Hạt nêm", "Nước mắm", "Đường", "Tiêu", "Muối", "Rượu vang trắng",
    "Gạo lứt", "Gạo thường", "Hành lá", "Ngò rí", "Nước tương Phú Sĩ", "Hạt nêm Aji-ngon® Nấm",
    "Topping cream", "Sữa tươi không đường", "Nước cốt dừa", "Cốm gạo lứt", "Đá bi", "Blendy® Trà Matcha Gạo Rang",
    "Trân châu khô", "Đường nâu", "Creamcheese", "Trà sữa Royal Blendy", "Húng lũi", "Nước cốt chanh", "Bột bánh rán pha sẵn"]
for name in ingredients:
    Ingredient.objects.get_or_create(name=name)
print("Nguyên liệu đã được thêm vào.")

admin_user = User.objects.get(username="admin")  # Lấy admin làm người tạo

# 4. Tạo công thức (Recipe) và gán DetailCategory
admin_user = User.objects.get(username="admin")
chef_user = User.objects.get(username="chef1")
user1 = User.objects.get(username="user1")
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

    {
        "name": "Mì ý xốt cua",
        "instructions": json.dumps([
            {"step": 1, "instruction": "Phi thơm tỏi băm với 20g bơ, xào săn thịt cua."},
            {"step": 2, "instruction": "Phi hành tỏi với 30g bơ, xào 2M gạch cua, nêm 2m Hạt nêm Aji-ngon® Heo."},
            {"step": 3, "instruction": "Thêm rượu vang trắng, xào 2 phút. Cho nước luộc mì, whipping cream, 1m đường, 50g sốt cà chua, 1m lá oregano, 1m nước mắm, đun sệt."},
            {"step": 4, "instruction": "Xay nhuyễn 1/2 thịt cua với xốt, giữ 1/2 để trang trí."},
            {"step": 5, "instruction": "Trộn mì ý với 1/2 xốt, rắc thịt cua, xốt, 20g phô mai parmesan, 1m lá oregano."}
        ]),
        "description": "Mì ý xốt cua là món ăn phong cách Âu với nước xốt cua thơm lừng, kết hợp vị béo ngậy của whipping cream và phô mai parmesan, dậy mùi lá oregano.",
        "cook_time": 30,
        "image": "recipe_images/mi_y_xot_cua.png",
        "author": admin_user,
        # "categories": ["Món Âu", "Bữa tối"],
    },

    {
    "name": "Cơm gạo lứt trộn",
    "instructions": json.dumps([
        {"step": 1, "instruction": "Gạo lứt vo sạch, ngâm với 200ml nước trong vòng 20 phút. Gạo thường vo sạch."},
        {"step": 2, "instruction": "Tỏi, hành tím băm nhuyễn. Cà rốt cắt hạt lựu. Bắp Mỹ tách lấy hạt. Đậu tước sơ cắt nhỏ 5mm. Nấm đông cô tươi bỏ gốc, rửa nhanh dưới vòi nước lạnh, cắt hạt lựu."},
        {"step": 3, "instruction": "Cho gạo và các nguyên liệu vào nồi cơm điện, nêm cùng 1/2m nước tương, 1/2m Hạt nêm Aji-ngon® Nấm vào nấu chín."},
        {"step": 4, "instruction": "Sau khi chín, cho hành lá vào trộn đều. Cho hành tỏi phi vào trộn đều cùng cơm."},
        {"step": 5, "instruction": "Trộn đều cơm với hỗn hợp rau củ, trang trí thêm ngò rí, ăn kèm nước tương 'Phú Sĩ'."}
    ]),
    "description": "Cơm gạo lứt trộn là món ăn bổ dưỡng và ngon miệng, sử dụng gạo lứt, cà rốt, bắp Mỹ, đậu cove và nấm đông cô tươi, rất thích hợp cho người ăn kiêng. Cơm gạo lứt thơm dịu, kết hợp rau củ tươi ngọt thanh mát, bổ sung nhiều lớp hương vị hấp dẫn. Mẹo: Cho thêm dầu ăn lúc nấu để hạt cơm bóng đẹp, ngâm gạo lứt trước để mềm, và luộc rau mở nắp để giữ màu xanh.",
    "cook_time": 30,
    "image": "recipe_images/com_gao_lut_tron.jpg",
    "author": admin_user,
    },

    {
    "name": "Trà sữa kem matcha",
    "instructions": json.dumps([
        {"step": 1, "instruction": "Đánh bông hỗn hợp topping gồm 70g kem topping, 40g sữa tươi không đường, 10g nước cốt dừa và 1m Blendy® Trà Matcha Gạo Rang. Đánh đến khi hỗn hợp đặc lại, bông lên và mịn."},
        {"step": 2, "instruction": "Pha Trà sữa Matcha gạo rang theo hướng dẫn trên bao bì."},
        {"step": 3, "instruction": "Cho đá bi vào ly, rót trà sữa, thêm kem matcha lên trên, rắc 10g cốm gạo lứt và thưởng thức."}
    ]),
    "description": "Trà sữa kem matcha với lớp kem bông mềm mại, thơm mùi trà xanh, đượm vị gạo rang và ngọt vừa phải. Kết hợp topping cốm gạo lứt giòn giòn, là thức uống lý tưởng cho fan matcha. Mẹo: Thêm sữa tươi để kem topping dẻo mịn, không quá đặc. Có thể thay bằng các vị trà sữa Blendy khác.",
    "cook_time": 10,
    "image": "recipe_images/tra_sua_kem_matcha.jpg",
    "author": admin_user,
    },

    {
    "name": "Pancake trà sữa trân châu",
    "instructions": json.dumps([
        {"step": 1, "instruction": "Làm trân châu đường đen: Đun sôi 1 lít nước, cho 150g trân châu khô vào nấu 15 phút. Ủ thêm 15 phút để trân châu nở. Rửa qua nước lạnh để trân châu không vón cục."},
        {"step": 2, "instruction": "Nấu 100g đường nâu với 100ml nước, khuấy tan, cho trân châu vào, nấu đến khi nước đường sánh lại thì tắt lửa."},
        {"step": 3, "instruction": "Làm bánh: Pha bột bánh rán pha sẵn với 1m nước cốt chanh và nước theo hướng dẫn trên bao bì. Đun nóng chảo không dính, đặt chảo lên khăn ướt để nguội bớt, rồi chuyển lại lên bếp, giảm nhỏ lửa. Đổ bột vào chảo, tạo bánh đường kính 8cm. Rán đến khi mặt bánh nổi bọt, viền se lại, lật bánh và rán thêm 30 giây. Tiếp tục rán hết bột."},
        {"step": 4, "instruction": "Làm xốt trà sữa creamcheese: Cho 60g creamcheese, 20g đường và 2 gói Trà sữa Royal Blendy vào âu, đánh ở tốc độ thấp đến khi nhuyễn. Thêm 150g whipping cream, đánh ở tốc độ vừa đến khi hòa quyện, rồi tăng tốc độ cao, đánh tới khi kem bông mềm."},
        {"step": 5, "instruction": "Xếp 1 bánh pancake lên dĩa, phết 1 lớp xốt trà sữa creamcheese, xếp thêm 1 lớp bánh và 1 lớp kem, tạo 3 lớp. Topping với trân châu đường đen."}
    ]),
    "description": "Pancake trà sữa trân châu biến tấu từ trân châu đường đen quốc dân, kết hợp xốt trà sữa creamcheese béo ngậy và bánh pancake mềm thơm. Món bánh lạ miệng, hấp dẫn cả nhà. Mẹo: Sên trân châu với lửa nhỏ để thấm vị đường. Đánh creamcheese với bột trà sữa trước khi thêm kem tươi để kem dễ hòa quyện.",
    "cook_time": 45,
    "image": "recipe_images/pancake_tra_sua_tran_chau.jpg",
    "author": admin_user,
    }

]

for i, r in enumerate(recipes):
    created, _ = Recipe.objects.get_or_create(name=r["name"], defaults=r)
#     created.category.set([i + 1])

categories_recipes = {
    "Đậu hũ chiên": ["Món chay", "Bữa sáng"],
    "Canh gà hầm sâm": ["Món giàu chất xơ", "Bữa tối"],
    "Bò lúc lắc": ["Món giàu protein", "Bữa tối"],
    "Súp bí đỏ": ["Món giàu chất xơ", "Bữa sáng"],
    "Mì ý xốt cua": ["Món Âu", "Bữa tối"],
    "Cơm gạo lứt trộn": ["Món chay", "Món ít calo", "Bữa trưa"],
    "Trà sữa kem matcha": ["Món tráng miệng", "Món đơn giản"],
    "Pancake trà sữa trân châu": ["Món tráng miệng", "Món ăn nhanh", "Bữa xế"]
}

for recipe_name, category_names in categories_recipes.items():
    recipe = Recipe.objects.get(name=recipe_name)
    category_objects = [DetailCategory.objects.get(name=category_name) for category_name in category_names]
    recipe.category.set(category_objects)
print("Danh mục món ăn đã được gán vào món ăn.")
print("Món ăn đã được thêm vào.")

# 5. Gán nguyên liệu vào công thức (RecipeIngredient)
recipe_ingredients = [
    {"recipe": "Đậu hũ chiên", "ingredient": "Đậu hũ", "quantity": "200g"},
    {"recipe": "Canh gà hầm sâm", "ingredient": "Thịt gà", "quantity": "1 con"},
    {"recipe": "Canh gà hầm sâm", "ingredient": "Gừng", "quantity": "1 nhánh"},
    {"recipe": "Bò lúc lắc", "ingredient": "Thịt bò", "quantity": "300g"},
    {"recipe": "Súp bí đỏ", "ingredient": "Khoai tây", "quantity": "200g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Cua thịt", "quantity": "600g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Mỳ Ý", "quantity": "250g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Bơ lạt", "quantity": "50g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Sốt cà chua đậm đặc", "quantity": "50g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Hành tỏi băm", "quantity": "10g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Nước luộc mì", "quantity": "1 chén"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Lá oregano", "quantity": "10g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Whipping cream", "quantity": "1 chén"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Phô mai parmesan", "quantity": "20g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Hạt nêm", "quantity": "8g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Nước mắm", "quantity": "3g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Đường", "quantity": "4g"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Tiêu", "quantity": "1/3m"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Muối", "quantity": "1/3m"},
    {"recipe": "Mì ý xốt cua", "ingredient": "Rượu vang trắng", "quantity": "1 ít"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Gạo thường", "quantity": "50g"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Tỏi", "quantity": "3 tép"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Hành tím", "quantity": "2 củ"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Cà rốt", "quantity": "50g"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Gạo lứt", "quantity": "100g"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Bắp Mỹ", "quantity": "1/3 trái"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Đậu Pháp", "quantity": "50g"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Nấm đông cô tươi", "quantity": "20g"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Hành lá", "quantity": "1 ít"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Ngò rí", "quantity": "1 ít"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Nước tương Phú Sĩ", "quantity": "1/2m"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Hạt nêm Aji-ngon® Nấm", "quantity": "1/2m"},
    {"recipe": "Cơm gạo lứt trộn", "ingredient": "Muối", "quantity": "1 ít"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Topping cream", "quantity": "70g"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Sữa tươi không đường", "quantity": "40g"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Nước cốt dừa", "quantity": "10g"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Cốm gạo lứt", "quantity": "10g"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Đá bi", "quantity": "1 ít"},
    {"recipe": "Trà sữa kem matcha", "ingredient": "Blendy® Trà Matcha Gạo Rang", "quantity": "1m"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Trân châu khô", "quantity": "150g"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Đường nâu", "quantity": "100g"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Whipping cream", "quantity": "150g"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Creamcheese", "quantity": "60g"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Trà sữa Royal Blendy", "quantity": "2 gói"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Đường", "quantity": "20g"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Húng lũi", "quantity": "1 ít"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Muối", "quantity": "1 ít"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Nước cốt chanh", "quantity": "1m"},
    {"recipe": "Pancake trà sữa trân châu", "ingredient": "Bột bánh rán pha sẵn", "quantity": "1 gói"},
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
    {"recipe": "Mì ý xốt cua", "user": "user1", "rating": 5, "comment": "Xốt cua béo ngậy, rất thơm!"},
    {"recipe": "Cơm gạo lứt trộn", "user": "user1", "rating": 4, "comment": "Món ăn nhẹ nhàng, phù hợp để ăn kiêng!"},   
    {"recipe": "Súp bí đỏ", "user": "user2", "rating": 4, "comment": "Ngon nhưng hơi ngọt."},
    {"recipe": "Đậu hũ chiên", "user": "user2", "rating": 5, "comment": "Rất thích món này!"},
    {"recipe": "Trà sữa kem matcha", "user": "user2", "rating": 1, "comment": "Nhìn màu trà sữa đã thấy không ngon rồi, mà mình muốn có công thức pha trà sữa riêng chứ không mua mua gói sẵn về pha ra đâu."},
    {"recipe": "Trà sữa kem matcha", "user": "user1", "rating": 3, "comment": "Mình đã làm thử ly trà sữa này thật sự không hợp với mình, trà sữa mà có nước cốt dừa và màu nước cũng không đẹp."},
    {"recipe": "Pancake trà sữa trân châu", "user": "user1", "rating": 5, "comment": "Món này hấp dẫn quá nè, nhưng nếu có thời gian để tự làm trân châu chắc còn ok hơn nữa!"},   
    {"recipe": "Pancake trà sữa trân châu", "user": "user2", "rating": 4, "comment": "Bánh hơi ngọt."},
]

for r in reviews:
    recipe = Recipe.objects.get(name=r["recipe"])
    user = User.objects.get(username=r["user"])
    Review.objects.create(recipe=recipe, user=user, rating=r["rating"], comment=r["comment"])
print("Đánh giá món ăn đã được thêm vào.")
