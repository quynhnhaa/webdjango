# Hướng dẫn Cài đặt và Chạy Dự án

## 1. Cài đặt các thư viện cần thiết
Trước tiên, bạn cần cài đặt tất cả các thư viện cần thiết bằng lệnh sau:
```sh
pip install -r requirements.txt
```

## 2. Migrate và Khởi tạo Dữ liệu
Sau khi migrate cơ sở dữ liệu, chạy file data_initial.sql trong mysql để khởi tạo dữ liệu

📂 *Bạn có thể xem nội dung chi tiết trong tập tin:*
```
data_initial.sql cùng cấp với manage.py
```

---

## 3. Thông tin về Module `Recipe`
📌 *Lưu ý:* Trường `instructions` lưu dưới dạng JSON.
### 🔹 Ví dụ về cách tạo một đối tượng `Recipe`
```python
import json
from recipes.models import Recipe

Recipe.objects.get_or_create(
    name="Đậu hũ chiên",
    defaults={
        "instructions": json.dumps([
            {"step": 1, "instruction": "Cắt đậu hũ thành miếng nhỏ."},
            {"step": 2, "instruction": "Chiên giòn đậu hũ với dầu ăn."}
        ]),
        "description": "Miếng đậu hũ mềm mịn bên trong, giòn rụm bên ngoài, thường được chiên vàng đều và dùng kèm với nước chấm chua ngọt hoặc mắm tỏi.",
        "cook_time": 10,
        "category": mon_chay,
        "image": "recipe_images/dau_hu_chien.jpg",
        "author": admin_user
    }
)
```


---
