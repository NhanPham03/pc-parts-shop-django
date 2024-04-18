from django.db import models
from apps.carts.models import Cart
from apps.items.models import Item

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, to_field='cart_id', related_name='cart_items')
  item = models.ForeignKey(Item, on_delete=models.CASCADE, to_field='item_id', related_name='cart_items')
  
  class Meta:
    db_table = 'cart_item'
    unique_together = (('cart', 'item'),)
