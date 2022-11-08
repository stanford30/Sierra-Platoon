from .models import Product
from django.db.models import Q


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating):
        products = Product.objects.filter(rating=rating)
        return products

    @classmethod
    def by_rating_range(cls, min, max):
        return Product.objects.filter(rating__range=(min, max))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating=rating, color=color)

    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) | Q(color=color))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()

    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by("category", "-price_cents")

    @classmethod
    def products_by_manufacturer_with_name_like(cls, name):
        return Product.objects.filter(manufacturer__icontains=name)

    @classmethod
    def manufacturer_names_for_query(cls, name):
        return Product.objects.filter(manufacturer__icontains=name)
