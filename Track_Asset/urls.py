from django.urls import path
from .views import CompanyList


urlpatterns = [
    path('company/', CompanyList.as_view(), name='comapny-list'),
    # path('company/create/', CompanyCreateAPIView.as_view(), name='company-create'),
]