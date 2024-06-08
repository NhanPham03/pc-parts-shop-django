from enum import Enum

class ProductTypes(Enum):
  CPU = 'CPU'
  GPU = 'GPU'
  RAM = 'RAM'
  PSU = 'PSU'
  Storage = 'Storage'
  Motherboard = 'Motherboard'
  Case = 'Case'
  Other = 'Other'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]
