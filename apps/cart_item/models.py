from django.db import models
from apps.carts.models import Cart
from apps.products.models import Product

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
  quantity = models.PositiveIntegerField(default=1)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  class Meta:
    db_table = 'cart_item'
