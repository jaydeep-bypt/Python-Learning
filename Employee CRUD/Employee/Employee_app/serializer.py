# employee/serializers.py

from rest_framework import serializers
from .models import Employee, Address, Department, Salary, Position

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
     department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
     position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all())

     class Meta:
         model = Employee
         fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
