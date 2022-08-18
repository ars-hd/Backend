from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
from api.serializers import EmployeeSerializer, ProductSerializer
from api.models import Employee, Product

# Create your views here.

@api_view(['GET'])
def helo(request):
    return Response({
        "msg": "Hello"
    })


@api_view(['GET'])
def employees(request):
    employee=Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)