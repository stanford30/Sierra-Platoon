from django.db import models

# Create your models here.
class User(models.Model):
    pass


class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(
        "Restaurant", on_delete=models.CASCADE, related_name="orders"
    )


class Restaurant(models.Model):
    pass


class FoodItem(models.Model):
    item = models.CharField(max_length=100, null=True)
    # order = models.ForeignKey(
    #     "Order", on_delete=models.CASCADE, null=True, related_name="food_items"
    # )
    orders = models.ManyToManyField(
        "Order", through="OrderFoodItem", related_name="food_items"
    )


class OrderFoodItem(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, null=True, related_name="order_food_items"
    )
    food_item = models.ForeignKey(
        "FoodItem", on_delete=models.CASCADE, null=True, related_name="order_food_items"
    )
