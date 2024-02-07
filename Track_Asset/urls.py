from django.urls import path
from .views import CompanyList, CompanyDetails, EmployeeList, EmployeeDetails, DeviceList, DeviceDetails


urlpatterns = [
    path('company/', CompanyList.as_view(), name='comapny-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetails.as_view(), name='employee-details'),
    path('device/', DeviceList.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetails.as_view(), name='device-details'),


]