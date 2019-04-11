from django.shortcuts import render
from rest_framework import generics
from.models import vendor
from .api.serializers import vendorSerializer, hiring_ticketSerializer

class vendorList(generics.ListCreateAPIView):
    queryset = vendor.objects.all()
    serializer_class = vendorSerializer

class vendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset: vendor.objects.all()
    serializer_class = vendorSerializer

class hiring_ticketList(generics.ListCreateAPIView):
    queryset = vendor.objects.all()
    serializer_class = hiring_ticketSerializer

class hiring_ticketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = vendor.objects.all()
    serializer_class = hiring_ticketSerializer