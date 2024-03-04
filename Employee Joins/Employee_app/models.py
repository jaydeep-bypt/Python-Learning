from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

class Position(models.Model):
    title = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    