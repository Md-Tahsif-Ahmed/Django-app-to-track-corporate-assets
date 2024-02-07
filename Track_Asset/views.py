from django.shortcuts import render
# from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import generics
from .models import Company, Employee, Device, Assignment
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, AssignmentSerializer

# Company views
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer





