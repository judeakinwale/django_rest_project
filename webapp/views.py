from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Staff
from .serilaizers import ItemSerializer, StaffSerializer

# Create your views here.

class ItemList(APIView):

  def get(self, request):
    item = Item.objects.all()
    serializer = ItemSerializer(item, many=True)
    return Response(serializer.data)
  
  def post(self):
    pass


class StaffList(APIView):

  def get(self, request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)
  
  def post(self):
    pass