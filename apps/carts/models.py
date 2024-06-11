from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User

class CartStatus(models.TextChoices):
  PENDING = 'PENDING', _('Pending')
  CHECKED_OUT = 'CHECKED_OUT', _('Checked Out')
  PAID = 'PAID', _('Paid')
  CANCELLED = 'CANCELLED', _('Cancelled')
  FAILED = 'FAILED', _('Failed')

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
  status = models.CharField(choices=CartStatus.choices, default=CartStatus.PENDING, max_length=20)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'carts'
