from rest_framework import serializers
from .models import Customer, Company, Invoice, Material

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'vat_id']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['number', 'sales_date', 'type', 'customer', 'company']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['number', 'category', 'price']