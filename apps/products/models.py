from django.db import models
from apps.product_types.enums import ProductType

class Product(models.Model):
  product_id = models.AutoField(primary_key=True)
  description = models.TextField(blank=True, null=True)
  name = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  type = models.CharField(choices=[(pt.name, pt.value) for pt in ProductType], max_length=255)  
  
  class Meta:
    db_table = 'products'
