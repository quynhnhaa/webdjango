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

########## TẠO NGUYÊN LIỆU ĐƯỢC THÊM VÀO Ở RECIPEINGREDIENT (ĐÂY KO CẦN) ###############
# # 3. Tạo nguyên liệu (Ingredient)
# ingredients = [
#     "Thịt gà", "Thịt bò", "Thịt heo", "Đậu hũ", "Cà rốt", "Khoai tây",
#     "Hành tím", "Tỏi", "Gừng", "Sữa đặc", "Bột mì", "Trứng gà",
#     "Nước mắm", "Dầu ăn", "Ớt", "Hành lá", "Bí đỏ", "Nấm rơm",
#     "Cải xanh", "Mì ống", "Phô mai", "Cá hồi", "Tôm", "Đường",
#     "Muối", "Tiêu", "Nước tương", "Bắp cải", "Dưa leo", "Xúc xích",
#     "Cà chua", "Sữa tươi", "Bột chiên giòn", "Lá chanh", "Sả"
# ]
# for name in ingredients:
#     Ingredient.objects.get_or_create(name=name)
# print("Đã thêm nguyên liệu.")

# 4. Tạo công thức (Recipe) và gán DetailCategory
admin_user = User.objects.get(username="admin")
chef_user = User.objects.get(username="chef1")
user1 = User.objects.get(username="user1")
recipes = [
        {
            "name": "Đậu hũ chiên giòn",
            "description": "Đậu hũ mềm bên trong, giòn bên ngoài, ăn với nước mắm tỏi ớt.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Cắt đậu hũ thành miếng vuông nhỏ."},
                {"step": 2, "instruction": "Chiên đậu hũ trong dầu nóng đến khi vàng giòn."},
                {"step": 3, "instruction": "Pha nước mắm tỏi ớt để chấm."}
            ]),
            "cook_time": 15,
            "image": "recipe_images/dau_hu_chien.jpg",
            "author": admin_user,
            "categories": ["Món chiên", "Món chay"]
        },
        {
            "name": "Canh bí đỏ nấu tôm",
            "description": "Món canh ngọt thanh từ bí đỏ và tôm tươi.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Gọt vỏ bí đỏ, cắt miếng nhỏ, luộc chín."},
                {"step": 2, "instruction": "Xay nhuyễn bí đỏ với nước luộc."},
                {"step": 3, "instruction": "Đun sôi lại, thêm tôm tươi đã bóc vỏ, nêm gia vị."}
            ]),
            "cook_time": 25,
            "image": "recipe_images/canh_bi_do_tom.jpg",
            "author": chef_user,
            "categories": ["Món soup", "Món giàu protein"]
        },
        {
            "name": "Thịt kho tàu",
            "description": "Thịt hầm mềm với trứng và nước dừa, đậm đà hương vị Tết.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ướp thịt heo với nước mắm, đường, tỏi trong 30 phút."},
                {"step": 2, "instruction": "Đun thịt với nước dừa, thêm trứng luộc."},
                {"step": 3, "instruction": "Kho nhỏ lửa đến khi thịt mềm và nước sệt."}
            ]),
            "cook_time": 90,
            "image": "recipe_images/thit_kho_tau.jpg",
            "author": admin_user,
            "categories": ["Món kho", "Món ngày Tết"]
        },
        {
            "name": "Mì Ý sốt bò băm",
            "description": "Món mì Ý thơm ngon với sốt thịt bò băm và phô mai.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Luộc mì Ý trong nước sôi, để ráo."},
                {"step": 2, "instruction": "Xào thịt bò băm với hành tím, tỏi, thêm sốt cà chua."},
                {"step": 3, "instruction": "Trộn mì với sốt, rắc phô mai lên trên."}
            ]),
            "cook_time": 30,
            "image": "recipe_images/mi_y_sot_bo_bam.jpg",
            "author": chef_user,
            "categories": ["Món Âu", "Món giàu protein"]
        },
        {
            "name": "Chả cá chiên",
            "description": "Chả cá dai ngon, chiên vàng thơm lừng.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Cắt cá thành miếng, ướp với tỏi, ớt, nước mắm."},
                {"step": 2, "instruction": "Chiên cá trong chảo dầu nóng đến khi vàng đều."}
            ]),
            "cook_time": 20,
            "image": "recipe_images/cha_ca_chien.jpg",
            "author": admin_user,
            "categories": ["Món chiên", "Món Việt Nam"]
        },
        {
            "name": "Gà nướng mật ong",
            "description": "Gà nướng vàng óng, thơm lừng với mật ong và gia vị.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ướp gà với mật ong, nước tương, tỏi, tiêu trong 1 giờ."},
                {"step": 2, "instruction": "Nướng gà trong lò ở 180°C trong 40 phút."}
            ]),
            "cook_time": 60,
            "image": "recipe_images/ga_nuong_mat_ong.jpg",
            "author": user1,
            "categories": ["Món nướng", "Món giàu protein"]
        },
        {
            "name": "Canh chua cá lóc",
            "description": "Món canh chua đặc trưng miền Nam với cá lóc và rau thơm.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Nấu nước dùng với cà chua, dứa, me."},
                {"step": 2, "instruction": "Thêm cá lóc đã làm sạch, đun sôi."},
                {"step": 3, "instruction": "Nêm gia vị, thêm rau thơm trước khi tắt bếp."}
            ]),
            "cook_time": 35,
            "image": "recipe_images/canh_chua_ca_loc.jpg",
            "author": admin_user,
            "categories": ["Món soup", "Món Việt Nam"]
        },
        {
            "name": "Tteokbokki",
            "description": "Bánh gạo cay Hàn Quốc với sốt đỏ đặc trưng.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Luộc bánh gạo trụng qua nước lạnh."},
                {"step": 2, "instruction": "Pha sốt với ớt bột, đường, nước tương."},
                {"step": 3, "instruction": "Xào bánh gạo với sốt đến khi sệt."}
            ]),
            "cook_time": 20,
            "image": "recipe_images/tteokbokki.jpg",
            "author": chef_user,
            "categories": ["Món Hàn Quốc", "Món xào"]
        },
        {
            "name": "Salad rau trộn",
            "description": "Món salad tươi mát với rau xanh và sốt dầu giấm.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Rửa sạch bắp cải, cà rốt, dưa leo, cắt nhỏ."},
                {"step": 2, "instruction": "Pha sốt với dầu ô liu, giấm, muối, tiêu."},
                {"step": 3, "instruction": "Trộn rau với sốt trước khi ăn."}
            ]),
            "cook_time": 10,
            "image": "recipe_images/salad_rau_tron.jpg",
            "author": user1,
            "categories": ["Món chay", "Món ít calo"]
        },
        {
            "name": "Bánh chuối hấp",
            "description": "Bánh chuối mềm ngọt, thơm mùi lá chuối.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Nghiền chuối chín, trộn với bột mì, đường, sữa đặc."},
                {"step": 2, "instruction": "Đổ hỗn hợp vào khuôn, bọc lá chuối."},
                {"step": 3, "instruction": "Hấp cách thủy trong 30 phút."}
            ]),
            "cook_time": 40,
            "image": "recipe_images/banh_chuoi_hap.jpg",
            "author": admin_user,
            "categories": ["Món hấp", "Món Việt Nam"]
        },
        {
            "name": "Thịt bò xào cần tây",
            "description": "Thịt bò mềm xào với cần tây giòn ngọt.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ướp thịt bò với nước tương, tỏi, tiêu."},
                {"step": 2, "instruction": "Xào thịt bò nhanh trên lửa lớn, thêm cần tây."}
            ]),
            "cook_time": 15,
            "image": "recipe_images/thit_bo_xao_can_tay.jpg",
            "author": chef_user,
            "categories": ["Món xào", "Món giàu protein"]
        },
        {
            "name": "Cá kho tộ",
            "description": "Cá kho đậm đà với nước mắm và tiêu trong nồi đất.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ướp cá với nước mắm, đường, tiêu, hành tím."},
                {"step": 2, "instruction": "Kho cá trong nồi đất với lửa nhỏ trong 1 giờ."}
            ]),
            "cook_time": 70,
            "image": "recipe_images/ca_kho_to.jpg",
            "author": admin_user,
            "categories": ["Món kho", "Món Việt Nam"]
        },
        {
            "name": "Gỏi gà xé phay",
            "description": "Gỏi gà trộn chua ngọt với rau răm và hành phi.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Luộc gà, xé nhỏ."},
                {"step": 2, "instruction": "Trộn gà với hành phi, rau răm, nước mắm chua ngọt."}
            ]),
            "cook_time": 20,
            "image": "recipe_images/goi_ga_xe_phay.jpg",
            "author": user1,
            "categories": ["Món Việt Nam", "Món giàu protein"]
        },
        {
            "name": "Sườn nướng BBQ",
            "description": "Sườn heo nướng với sốt BBQ đậm đà.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ướp sườn với sốt BBQ, tỏi, mật ong trong 2 giờ."},
                {"step": 2, "instruction": "Nướng sườn trong lò 200°C trong 45 phút."}
            ]),
            "cook_time": 60,
            "image": "recipe_images/suon_nuong_bbq.jpg",
            "author": chef_user,
            "categories": ["Món nướng", "Món Âu"]
        },
        {
            "name": "Chè đậu xanh",
            "description": "Chè đậu xanh ngọt mát, thơm mùi lá dứa.",
            "instructions": json.dumps([
                {"step": 1, "instruction": "Ngâm đậu xanh 2 giờ, nấu chín với nước."},
                {"step": 2, "instruction": "Thêm đường, lá dứa, nấu đến khi sệt."}
            ]),
            "cook_time": 45,
            "image": "recipe_images/che_dau_xanh.jpg",
            "author": admin_user,
            "categories": ["Món Việt Nam", "Bữa xế"]
        },
    ]
for r in recipes:
    recipe, created = Recipe.objects.get_or_create(
        name=r["name"],
        defaults={
            "description": r["description"],
            "instructions": r["instructions"],
            "cook_time": r["cook_time"],
            "image": r["image"],
            "author": r["author"]
        }
    )
    detail_categories = DetailCategory.objects.filter(name__in=r["categories"])
    recipe.category.set(detail_categories)
    recipe.save()
    print(f"Đã thêm công thức: {r['name']} với categories: {r['categories']}")

# 5. Gán nguyên liệu vào công thức (RecipeIngredient)
recipe_ingredients = [
    {"recipe": "Đậu hũ chiên giòn", "ingredient": "Đậu hũ", "quantity": "200g"},
    {"recipe": "Đậu hũ chiên giòn", "ingredient": "Dầu ăn", "quantity": "50ml"},
    {"recipe": "Đậu hũ chiên giòn", "ingredient": "Nước mắm", "quantity": "1 muỗng canh"},
    {"recipe": "Canh bí đỏ nấu tôm", "ingredient": "Bí đỏ", "quantity": "300g"},
    {"recipe": "Canh bí đỏ nấu tôm", "ingredient": "Tôm", "quantity": "150g"},
    {"recipe": "Thịt kho tàu", "ingredient": "Thịt heo", "quantity": "500g"},
    {"recipe": "Thịt kho tàu", "ingredient": "Trứng gà", "quantity": "4 quả"},
    {"recipe": "Thịt kho tàu", "ingredient": "Nước mắm", "quantity": "2 muỗng canh"},
    {"recipe": "Mì Ý sốt bò băm", "ingredient": "Mì ống", "quantity": "200g"},
    {"recipe": "Mì Ý sốt bò băm", "ingredient": "Thịt bò", "quantity": "250g"},
    {"recipe": "Mì Ý sốt bò băm", "ingredient": "Phô mai", "quantity": "50g"},
    {"recipe": "Chả cá chiên", "ingredient": "Cá hồi", "quantity": "300g"},
    {"recipe": "Chả cá chiên", "ingredient": "Dầu ăn", "quantity": "50ml"},
    {"recipe": "Gà nướng mật ong", "ingredient": "Thịt gà", "quantity": "500g"},
    {"recipe": "Gà nướng mật ong", "ingredient": "Nước tương", "quantity": "2 muỗng canh"},
    {"recipe": "Canh chua cá lóc", "ingredient": "Cá hồi", "quantity": "400g"},
    {"recipe": "Canh chua cá lóc", "ingredient": "Cà chua", "quantity": "2 quả"},
    {"recipe": "Tteokbokki", "ingredient": "Bột mì", "quantity": "200g"},
    {"recipe": "Tteokbokki", "ingredient": "Ớt", "quantity": "1 muỗng canh"},
    {"recipe": "Salad rau trộn", "ingredient": "Bắp cải", "quantity": "100g"},
    {"recipe": "Salad rau trộn", "ingredient": "Cà rốt", "quantity": "50g"},
    {"recipe": "Bánh chuối hấp", "ingredient": "Bột mì", "quantity": "150g"},
    {"recipe": "Bánh chuối hấp", "ingredient": "Sữa đặc", "quantity": "100ml"},
    {"recipe": "Thịt bò xào cần tây", "ingredient": "Thịt bò", "quantity": "200g"},
    {"recipe": "Thịt bò xào cần tây", "ingredient": "Cải xanh", "quantity": "100g"},
    {"recipe": "Cá kho tộ", "ingredient": "Cá hồi", "quantity": "300g"},
    {"recipe": "Cá kho tộ", "ingredient": "Nước mắm", "quantity": "2 muỗng canh"},
    {"recipe": "Gỏi gà xé phay", "ingredient": "Thịt gà", "quantity": "300g"},
    {"recipe": "Gỏi gà xé phay", "ingredient": "Hành lá", "quantity": "2 nhánh"},
    {"recipe": "Sườn nướng BBQ", "ingredient": "Thịt heo", "quantity": "500g"},
    {"recipe": "Sườn nướng BBQ", "ingredient": "Đường", "quantity": "2 muỗng canh"},
    {"recipe": "Chè đậu xanh", "ingredient": "Đậu hũ", "quantity": "200g"},
    {"recipe": "Chè đậu xanh", "ingredient": "Đường", "quantity": "100g"},
]
for ri in recipe_ingredients:
    recipe = Recipe.objects.get(name=ri["recipe"])
    ingredient = Ingredient.objects.get_or_create(name=ri["ingredient"])
    RecipeIngredient.objects.get_or_create(
        recipe=recipe,
        ingredient=ingredient,
        quantity=ri["quantity"]
    )
print("Đã gán nguyên liệu vào công thức.")
