from django.urls import path
from .views import CompanyList, CompanyDetails


urlpatterns = [
    path('company/', CompanyList.as_view(), name='comapny-list'),
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company-details'),
]