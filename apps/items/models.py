from django.db import models
from apps.products.models import Product

class Item(models.Model):
  quantity = models.IntegerField(default=0)
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
  
  class Meta:
    db_table = 'items'
