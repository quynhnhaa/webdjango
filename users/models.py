from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  # Kế thừa từ AbstractUser để có sẵn username, email, password
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username