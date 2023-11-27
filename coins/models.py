from django.db import models
import django.utils.timezone
from typing import Any
    
class CryptoPrice(models.Model):
    symbol = models.CharField('Name', unique=True, max_length=100)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField('Date', auto_now_add=True)
    
    def __str__(self):
        return f"{self.symbol} - {self.price} USD"
