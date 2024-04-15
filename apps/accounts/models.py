from django.db import models
from apps.users.models import User

class Account(models.Model):
  account_id = models.AutoField(primary_key=True)
  username = models.CharField(unique=True, max_length=30)
  password = models.CharField(max_length=30)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id', related_name='accounts')
  
  class Meta:
    db_table = 'accounts'
