from rest_framework import serializers
from .models import Item, Staff


class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = Item
    fields ='__all__'


class StaffSerializer(serializers.ModelSerializer):

  class Meta:
    model = Staff
    fields ='__all__'