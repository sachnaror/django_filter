# models.py

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
