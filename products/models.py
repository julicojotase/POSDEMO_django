from django.db import models


class Product(models.Model):

    barcode = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.IntegerField(default=0)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Stock: {self.stock}"