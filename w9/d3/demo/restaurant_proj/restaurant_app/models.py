from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(
        "Category", related_name="items", on_delete=models.CASCADE
    )
