from django.db import models
from products.models import Product
from django.conf import settings


class FavoritesManager(models.Manager):
    pass


class Favorites(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product'
    )
    substitute = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='substitute',
    )

    objects = FavoritesManager()

    class Meta:
        db_table = 'favorites_favorites'
        constraints = [
            models.UniqueConstraint(fields=['user', 'product', 'substitute'], name='unique combination')
        ]
