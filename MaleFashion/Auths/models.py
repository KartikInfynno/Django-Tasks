from django.db import models
from django.contrib.auth.models import AbstractUser


user_type = (
    ('Seller Account', 'Seller Account'),
    ('Buyer Account', 'Buyer Account'),
)


class My_User(AbstractUser):
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=255,choices=user_type,default='Buyer Account')

    def __str__(self):
        return self.username
