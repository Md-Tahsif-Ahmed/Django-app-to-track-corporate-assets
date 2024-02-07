from django.db import models

# create Company Model
class Company(models.Model):
    name = models.CharField(max_length=100)
    

# create Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    designation=models.CharField(max_length=100)

# create Device Model
class Device(models.Model):
    type=models.CharField(max_length=50)
    model=models.CharField(max_length=100)
    serial_no=models.CharField(max_length=100)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)

# create Assignment Model
class Assignment(models.Model):
    device=models.ForeignKey(Device, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date=models.DateTimeField()
    return_date=models.DateTimeField(null=True, blank=True)
    condition_on_checkout=models.TextField()
    condition_on_return=models.TextField(null=True, blank=True)




