1. Cài đặt các thư viện cần thiết:
   pip install -r requirements.txt
2. Sau khi đã migrate thì chạy lệnh:
   python3 manage.py populate_db
   Mục đích: Taọ dữ liệu trước khi chạy web. Chỉ cần chạy 1 lần đầu tiên duy nhất.
   Có thể xem nội dung file ở recipes/managemnent/commands
3. Module Recipe:
   Có thuộc tinh instructions = models.TextField(). Lưu ý instructions lưu dữ liệu dạng json.
   Ví dụ khi tạo một đối tượng recipe:
   Recipe.objects.get_or_create(
    name="Đậu hũ chiên",
    defaults={
        "instructions": json.dumps([
            {"step": 1, "instruction": "Cắt đậu hũ thành miếng nhỏ."},
            {"step": 2, "instruction": "Chiên giòn đậu hũ với dầu ăn."}
        ]),
        "description": "Miếng đậu hũ mềm mịn bên trong, giòn rụm bên ngoài, thường được chiên vàng đều và dùng kèm với nước chấm chua ngọt hoặc mắm tỏi",
        "cook_time": 10,
        "category": mon_chay,
        "image": "recipe_images/dau_hu_chien.jpg",
        "author": admin_user
    }
)
