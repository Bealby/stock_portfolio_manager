from django.db import models
from django.db.models.fields import DateField


class Trade(models.Model):
    symbol = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    iexId = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    holding_value = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total_profit_loss = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    volume = models.DecimalField(max_digits=20, decimal_places=0, null=False, default=0)
    buy_value = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    sell_value = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    profit_loss = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)

    def __str__(self):
        return self.name
