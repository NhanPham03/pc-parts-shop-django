from django.db import models
from apps.users.models import User

class Cart(models.Model):
  cart_id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id', related_name='carts')
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'carts'
