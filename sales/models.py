from django.db import models
from django.conf import settings
from products.models import Product
from cash.models import CashRegister

User = settings.AUTH_USER_MODEL


class Sale(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    cash = models.ForeignKey(CashRegister, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    paid = models.DecimalField(max_digits=10, decimal_places=2)

    change = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total(self):

        total = sum(item.subtotal for item in self.items.all())

        self.total = total

        self.change = self.paid - total

        self.save()

    def __str__(self):

        return f"Venta {self.id}"
    
class SaleItem(models.Model):

    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):

        self.subtotal = self.quantity * self.price

        product = self.product

        product.stock -= self.quantity

        product.save()

        super().save(*args, **kwargs)

        self.sale.calculate_total()

    def __str__(self):

        return f"{self.product.name} x {self.quantity}"