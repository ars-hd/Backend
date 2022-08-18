from ast import Mod
from dataclasses import fields
from api.models import Employee, Product
from rest_framework.serializers import ModelSerializer
class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'