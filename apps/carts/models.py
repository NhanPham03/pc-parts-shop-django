from django.db import models
from apps.users.models import User

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'carts'
