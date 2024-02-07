from django.urls import path
from .views import CompanyList, CompanyDetails, EmployeeList


urlpatterns = [
    path('company/', CompanyList.as_view(), name='comapny-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
]