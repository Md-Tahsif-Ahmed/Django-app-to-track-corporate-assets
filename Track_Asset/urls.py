from django.urls import path
from .views import CompanyList, CompanyDetails, EmployeeList, EmployeeDetails, DeviceList, DeviceDetails, AssignmentList, AssignmentDetails
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title = "Asset Tracking API")
urlpatterns = [
    path('company/', CompanyList.as_view(), name='comapny-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetails.as_view(), name='employee-details'),
    path('device/', DeviceList.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetails.as_view(), name='device-details'),
    path('assignment/', AssignmentList.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentDetails.as_view(), name='assignment-details'),
    path('swagger-docs/', schema_view),
    # path('phone-company/', PhoneCompanyList.as_view(), name='phone-comapny-list'),




]