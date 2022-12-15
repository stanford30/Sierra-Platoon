from rest_framework import serializers
from .models import Category, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "description", "category", "price"]


class CategorySerializer(serializers.ModelSerializer):
    # items = ItemSerializer(
    #     "items",
    #     many=True,
    # )
    # items = ItemSerializer(many=True, read_only=True)
    items = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "description", "items"]
