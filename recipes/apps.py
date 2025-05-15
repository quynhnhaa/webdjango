from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self):
        from reviews.models import Review
        from . import cf_models
        import numpy as np

        try:
            reviews = Review.objects.all().values()
            Y_data = np.array([[r.get('user_id'), r.get("recipe_id"), r.get("rating")] for r in reviews])

            # Khởi tạo CF instance và lưu vào biến toàn cục hoặc cache
            cf_models.global_cf_instance = cf_models.CF(Y_data)
        except Exception as e:
            print(f"Error initializing CF: {e}")
        print(" CF initialized at startup!")