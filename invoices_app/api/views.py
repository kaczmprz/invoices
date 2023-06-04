from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Company, Invoice, Material
from .serializers import CustomerSerializer, CompanySerializer, MaterialSerializer, InvoiceSerializer
from django.core.exceptions import ValidationError

@api_view(['GET'])
def customer(request):
    if request.method == 'GET':
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def material(request):
    if request.method == 'GET':
        queryset = Material.objects.all()
        serializer = MaterialSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def company(request):
    if request.method == 'GET':
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def invoice(request):
    if request.method == 'GET':
        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset, many=True)
        return Response(serializer.data)

