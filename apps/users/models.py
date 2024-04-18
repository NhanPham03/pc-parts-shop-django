from django.db import models

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255, default='')
  last_name = models.CharField(max_length=255, default='')
  email = models.EmailField(default='')
  address = models.CharField(max_length=255, default='')
  birthdate = models.DateField(blank=True, default=None)
  city = models.CharField(max_length=255, default='')
  country = models.CharField(max_length=255, default='')
  
  class Meta:
    db_table = 'users'
