from django.db import models
from apps.products.enums import ProductTypes

class Product(models.Model):
  description = models.TextField(default='')
  name = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  type = models.CharField(choices=ProductTypes.choices(), max_length=20)  
  
  class Meta:
    db_table = 'products'
