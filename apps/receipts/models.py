from django.db import models
from apps.carts.models import Cart
from apps.users.models import User

class Receipt(models.Model):
  receipt_id = models.AutoField(primary_key=True)
  created_at = models.DateTimeField(auto_now_add=True)
  total = models.FloatField(default=0)
  cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, to_field='cart_id', related_name='receipts')
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id', related_name='receipts')
  
  class Meta:
    db_table = 'receipts'
