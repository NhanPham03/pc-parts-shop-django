from django.db import models
from apps.product_types.enums import ProductType

class Product(models.Model):
  description = models.TextField(default='')
  name = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  type = models.CharField(choices=[(pt.name, pt.value) for pt in ProductType], max_length=255)  
  
  class Meta:
    db_table = 'products'
