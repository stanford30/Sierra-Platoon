from django.db import models

# Create your models here.
class Shop(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="shop")
    # product = models.ForeignKey(
    #     "Product", on_delete=models.CASCADE, related_name="shop", null=True
    # )
    # products = models.ManyToManyField("Product")


class Product(models.Model):
    shop = models.ForeignKey(
        "Shop", on_delete=models.CASCADE, related_name="products", null=True
    )
    # review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True)


class Review(models.Model):
    review = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="reviews", null=True
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, null=True, related_name="reviews"
    )


class User(models.Model):
    reviewed_product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="user", null=True
    )
