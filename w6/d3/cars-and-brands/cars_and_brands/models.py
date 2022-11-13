from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    brand_logo_url = models.URLField(null=True)
    country = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name="cars")
