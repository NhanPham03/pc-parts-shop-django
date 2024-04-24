from django.db import models
from apps.carts.models import Cart
from apps.users.models import User

class Receipt(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  total = models.FloatField(default=0)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='receipts')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receipts')
  
  class Meta:
    db_table = 'receipts'
