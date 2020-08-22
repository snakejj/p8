from django.db import models

import random


class ProductManager(models.Manager):
    def create_products_from_openfoodfacts(self, products):
        """Get the products from initdb et put in DB with ORM"""

        Product.objects.all().delete()
        Category.objects.all().delete()

        for categ in products:
            category, iscreated = Category.objects.get_or_create(name=categ)

            for fullp in products[categ]:
                product, iscreated = Product.objects.get_or_create(
                    code=fullp.get("code"), defaults={
                        "product_name": fullp.get("product_name"),
                        "product_url": fullp.get("product_url"),
                        "nutrition_grade_fr": fullp.get("nutrition_grade_fr"),
                        "image_url": fullp.get("image_url"),
                        "image_nutrition_url": fullp.get("image_nutrition_url"),
                        "category": category, }
                )


class Category(models.Model):
    name = models.CharField("category name", max_length=100)

    objects = ProductManager()


class Product(models.Model):
    code = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=80)
    nutrition_grade_fr = models.CharField(max_length=1)
    image_url = models.URLField("image url")
    image_nutrition_url = models.URLField("image nutrition url")
    product_url = models.URLField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    objects = ProductManager()



