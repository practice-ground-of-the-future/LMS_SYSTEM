from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):

    """Модель описывающая пользователя"""

    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.username


