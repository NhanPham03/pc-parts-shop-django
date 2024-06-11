from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductTypes(models.TextChoices):
  CPU = 'CPU', _('CPU')
  GPU = 'GPU', _('GPU')
  RAM = 'RAM', _('RAM')
  PSU = 'PSU', _('PSU')
  STORAGE = 'STORAGE', _('Storage')
  MOTHERBOARD = 'MOTHERBOARD', _('Motherboard')
  CASE = 'CASE', _('Case')
  OTHER = 'OTHER', _('Other')

class Product(models.Model):
  description = models.TextField(default='')
  name = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  type = models.CharField(choices=ProductTypes.choices, max_length=20)  
  
  class Meta:
    db_table = 'products'
