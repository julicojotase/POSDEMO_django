from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class CashRegister(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    opened_at = models.DateTimeField(default=timezone.now)

    closed_at = models.DateTimeField(null=True, blank=True)

    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)

    final_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    is_open = models.BooleanField(default=True)

    def close(self, amount):

        self.final_amount = amount
        self.closed_at = timezone.now()
        self.is_open = False

        self.save()

    def __str__(self):

        return f"Caja {self.id} - {self.user}"