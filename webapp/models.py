from django.db import models
from django.utils.timezone import now as tzn
from .managers import FreeItemManager

# Create your models here.

class Item(models.Model):

  name = models.CharField(max_length=250)
  description = models.TextField(null=True, blank=True)
  price = models.FloatField(default=0.00)
  quantity = models.IntegerField(null=True, blank=True)
  is_published = models.BooleanField(default=True)
  timestamp = models.DateTimeField(default=tzn)

  objects = models.Manager()
  free = FreeItemManager()

  def __str__(self):
      return self.name


class Staff(models.Model):

  first_name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  description = models.TextField(null=True, blank=True)
  timestamp = models.DateTimeField(default=tzn)

  def __str__(self):
      return f"{self.first_name} {self.last_name}"