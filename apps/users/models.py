from django.db import models

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  address = models.CharField(max_length=255, blank=True, null=True)
  birthdate = models.DateField(blank=True, null=True)
  city = models.CharField(max_length=255, blank=True, null=True)
  country = models.CharField(max_length=255, blank=True, null=True)
  
  class Meta:
    db_table = 'users'
