from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
  def create_user(self, username, password=None, **extra_fields):
    if not username:
      raise ValueError('The username field must be set')
    user = self.model(username=username, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, password, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(unique=True, max_length=30)
  password = models.CharField(max_length=30)
  first_name = models.CharField(max_length=255, default='')
  last_name = models.CharField(max_length=255, default='')
  email = models.EmailField(default='')
  address = models.CharField(max_length=255, default='')
  birthdate = models.DateField(blank=True, null=True)
  city = models.CharField(max_length=255, default='')
  country = models.CharField(max_length=255, default='')

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'username'

  class Meta:
    db_table = 'users'
